from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession

from .database import async_session


async def get_db() -> AsyncIterator[AsyncSession]:
    async with async_session() as session:
        yield session
