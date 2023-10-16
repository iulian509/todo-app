import pytest
from common.database import Base
from common.dependencies import get_db
from httpx import AsyncClient
from main import app
from tests.database import engine, override_get_db

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
async def test_client():
    async_client = AsyncClient(app=app, base_url="http://localhost")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield async_client
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="module")
def anyio_backend():
    return "asyncio"
