from config import testing_settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(testing_settings.SQLALCHEMY_DATABASE_URL, future=True)

testing_async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


async def override_get_db() -> AsyncSession:
    async with testing_async_session() as session:
        yield session
