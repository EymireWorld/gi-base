import hashlib
from collections.abc import Awaitable, Callable
from typing import Any

from fastapi import Request, Response


def default_key_builder(
    func: Callable[..., Any | Awaitable[Any]],
    prefix: str,
    request: Request,
    response: Response,
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
) -> str:
    cache_key = hashlib.md5(
        f'{func.__module__}:{func.__name__}:{args}:{kwargs}'.encode()
    ).hexdigest()

    return f'{prefix}:{cache_key}'
