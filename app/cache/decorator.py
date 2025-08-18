import pickle
from collections.abc import Awaitable, Callable
from functools import wraps
from inspect import Parameter, Signature, iscoroutinefunction
from typing import Any

from fastapi import Request, Response
from fastapi.concurrency import run_in_threadpool

from . import CacheStorage


__all__ = ['cache']


def find_dependency(signature: Signature, annotation: Any) -> Parameter | None:
    for param in signature.parameters.values():
        if param.annotation == annotation:
            return param


async def run_func(
    func: Callable[..., Any | Awaitable[Any]],
    *args: tuple[Any, ...],
    **kwargs: dict[str, Any],
):
    if iscoroutinefunction(func):
        return await func(*args, **kwargs)
    else:
        return await run_in_threadpool(func, *args, **kwargs)


def cache(
    expire: int = 1800,
    ignore_kwargs: list[str] | None = None,
):
    def decorator(func: Callable[..., Any | Awaitable[Any]]):
        signature = Signature.from_callable(func)
        is_request_param_injected = False
        request_param = find_dependency(signature, Request)
        is_response_param_injected = False
        response_param = find_dependency(signature, Response)

        if request_param is None:
            is_request_param_injected = True
            request_param = Parameter(
                name='request',
                kind=Parameter.KEYWORD_ONLY,
                annotation=Request,
            )
            signature = signature.replace(
                parameters=[
                    *signature.parameters.values(),
                    request_param,
                ]
            )
        if response_param is None:
            is_response_param_injected = True
            response_param = Parameter(
                name='response',
                kind=Parameter.KEYWORD_ONLY,
                annotation=Response,
            )
            signature = signature.replace(
                parameters=[
                    *signature.parameters.values(),
                    response_param,
                ]
            )

        @wraps(func)
        async def wrapper(*args: tuple[Any, ...], **kwargs: dict[str, Any]):
            kwargs_copy = kwargs.copy()

            request: Request = kwargs_copy.pop(request_param.name)  # type: ignore
            response: Response = kwargs_copy.pop(response_param.name)  # type: ignore

            if ignore_kwargs:
                for kwarg in ignore_kwargs:
                    kwargs_copy.pop(kwarg)

            if is_request_param_injected:
                kwargs.pop(request_param.name)
            if is_response_param_injected:
                kwargs.pop(response_param.name)

            backend = CacheStorage.get_backend()
            prefix = CacheStorage.get_prefix()
            key_builder = CacheStorage.get_key_builder()

            cache_key = key_builder(
                func,
                prefix,
                request,
                response,
                args,
                kwargs_copy,
            )

            cached = await backend.get(cache_key)

            if cached is None:
                result = await run_func(func, *args, **kwargs)

                await backend.set(cache_key, pickle.dumps(result), expire)
            else:
                result = pickle.loads(cached)

            return result

        wrapper.__signature__ = signature  # type: ignore

        return wrapper

    return decorator
