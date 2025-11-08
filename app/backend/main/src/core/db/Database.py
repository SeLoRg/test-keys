from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession


class Database:
    def __init__(self, url: str, echo: bool = False):
        self._async_engine = create_async_engine(url=url, echo=echo)
        self._async_session_factory = async_sessionmaker(
            bind=self._async_engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._async_session_factory() as sess:
            yield sess

    @property
    def get_async_session_factory(self):
        return self._async_session_factory
