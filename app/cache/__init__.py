from app.cache.key_builder import default_key_builder
from app.cache.types import Backend, KeyBuilder


class CacheStorage:
    _init: bool = False
    _backend: Backend | None = None
    _prefix: str | None = None
    _key_builder: KeyBuilder | None = None

    @classmethod
    def init(
        cls,
        backend: Backend,
        prefix: str = 'fastapi-cache',
        key_builder: KeyBuilder | None = None,
    ) -> None:
        if cls._init:
            return

        cls._init = True
        cls._backend = backend
        cls._prefix = prefix
        cls._key_builder = key_builder if key_builder else default_key_builder

    @classmethod
    def get_backend(cls) -> Backend:
        if not cls._init:
            raise Exception('You need init cache storage!')

        return cls._backend

    @classmethod
    def get_prefix(cls) -> str:
        if not cls._init:
            raise Exception('You need init cache storage!')

        return cls._prefix

    @classmethod
    def get_key_builder(cls) -> KeyBuilder:
        if not cls._init:
            raise Exception('You need init cache storage!')

        return cls._key_builder
