import pytest
from common.constants import (
    BAD_REQUEST,
    NOT_FOUND,
    PRIORITY_VALUE_ERROR,
    VALUE_AREADY_EXISTS,
)
from tests.constants import (
    TEST_ID,
    TEST_INPUT,
    TEST_INVALID_INPUT,
    TEST_RESPONSE,
    TEST_UPDATE_INPUT,
    TEST_UPDATE_RESPONSE,
    TEST_WRONG_ID,
)

from fastapi import status


@pytest.mark.anyio
async def test_create_todo(test_client):
    response = await test_client.post("/todos/", json=TEST_INPUT)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == TEST_RESPONSE


@pytest.mark.anyio
async def test_create_todo_invalid_priority(test_client):
    response = await test_client.post("/todos/", json=TEST_INVALID_INPUT)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json().get("detail") == BAD_REQUEST.format(PRIORITY_VALUE_ERROR)


@pytest.mark.anyio
async def test_create_todo_integrity_error(test_client):
    response = await test_client.post("/todos/", json=TEST_INPUT)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json().get("detail") == BAD_REQUEST.format(VALUE_AREADY_EXISTS)


@pytest.mark.anyio
async def test_get_todos(test_client):
    response = await test_client.get("/todos/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [TEST_RESPONSE]


@pytest.mark.anyio
async def test_get_todo(test_client):
    response = await test_client.get(f"/todos/{TEST_ID}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == TEST_RESPONSE


@pytest.mark.anyio
async def test_get_todo_not_found(test_client):
    response = await test_client.get(f"/todos/{TEST_WRONG_ID}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json().get("detail") == NOT_FOUND


@pytest.mark.anyio
async def test_update_todo(test_client):
    response = await test_client.put(f"/todos/{TEST_ID}", json=TEST_UPDATE_INPUT)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == TEST_UPDATE_RESPONSE


@pytest.mark.anyio
async def test_update_todo_not_found(test_client):
    response = await test_client.put(f"/todos/{TEST_WRONG_ID}", json=TEST_UPDATE_INPUT)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json().get("detail") == NOT_FOUND


@pytest.mark.anyio
async def test_delete_todo(test_client):
    response = await test_client.delete(f"/todos/{TEST_ID}")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.anyio
async def test_delete_todo_not_fount(test_client):
    response = await test_client.delete(f"/todos/{TEST_WRONG_ID}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json().get("detail") == NOT_FOUND
