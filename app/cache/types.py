import abc
from collections.abc import Awaitable, Callable
from typing import Any

from fastapi import Request, Response


class Backend(abc.ABC):
    @abc.abstractmethod
    async def get(self, key: str) -> bytes | None: ...

    @abc.abstractmethod
    async def set(self, key: str, value: bytes, expire: int) -> bool: ...

    @abc.abstractmethod
    async def clear(self, key: str) -> bool: ...


KeyBuilder = Callable[
    [
        Callable[..., Any | Awaitable[Any]],
        str,
        Request,
        Response,
        tuple[Any, ...],
        dict[str, Any],
    ],
    str,
]
