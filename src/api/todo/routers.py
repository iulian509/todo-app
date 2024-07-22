from common.dependencies import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from todo.schemas import TodoCreateSchema, TodoSchema, TodoUpdateSchema
from todo.handlers import create, delete, get, list_all, update

router = APIRouter()


@router.post("/todos/", response_model=TodoSchema)
async def create_todo(
    todo: TodoCreateSchema, db_session: AsyncSession = Depends(get_db)
) -> TodoSchema:
    task = await create(todo, db_session)
    return task


@router.get("/todos/", response_model=list[TodoSchema])
async def read_todos(db_session: AsyncSession = Depends(get_db)) -> list[TodoSchema]:
    tasks = await list_all(db_session)
    return tasks


@router.get("/todos/{todo_id}", response_model=TodoSchema)
async def read_todo(
    todo_id: int, db_session: AsyncSession = Depends(get_db)
) -> TodoSchema:
    task = await get(todo_id, db_session)
    return task


@router.put("/todos/{todo_id}", response_model=TodoSchema)
async def update_todo(
    todo_id: int, todo: TodoUpdateSchema, db_session: AsyncSession = Depends(get_db)
) -> TodoSchema:
    task = await update(todo_id, todo, db_session)
    return task


@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, db_session: AsyncSession = Depends(get_db)):
    await delete(todo_id, db_session)
