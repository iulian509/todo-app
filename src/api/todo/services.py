from common.constants import (
    BAD_REQUEST,
    HTTP_400,
    HTTP_404,
    NOT_FOUND,
    VALUE_AREADY_EXISTS,
)
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from todo.models import TodoModel
from todo.schemas import TodoCreateSchema, TodoUpdateSchema


async def get(todo_id: int, db_session: AsyncSession):
    db_task = await db_session.execute(
        select(TodoModel).filter(TodoModel.id == todo_id)
    )
    db_task_result = db_task.scalars().one_or_none()
    if db_task_result is None:
        raise HTTPException(status_code=HTTP_404, detail=NOT_FOUND)
    return db_task_result


async def list_all(db_session: AsyncSession):
    db_tasks = await db_session.execute(
        select(TodoModel).order_by(TodoModel.priority.asc())
    )
    return db_tasks.scalars().all()


async def create(todo: TodoCreateSchema, db_session: AsyncSession):
    try:
        db_task = TodoModel(title=todo.title, priority=todo.priority)
        db_session.add(db_task)
        await db_session.commit()
        return db_task
    except ValueError as error:
        raise HTTPException(status_code=HTTP_400, detail=BAD_REQUEST.format(error))
    except IntegrityError:
        raise HTTPException(
            status_code=HTTP_400, detail=BAD_REQUEST.format(VALUE_AREADY_EXISTS)
        )


async def update(todo_id: int, todo: TodoUpdateSchema, db_session: AsyncSession):
    try:
        db_task = await get(todo_id, db_session)

        for var, value in vars(todo).items():
            setattr(db_task, var, value) if value else None

        db_session.add(db_task)
        await db_session.commit()

        return db_task
    except IntegrityError:
        raise HTTPException(
            status_code=HTTP_400, detail=BAD_REQUEST.format(VALUE_AREADY_EXISTS)
        )


async def delete(todo_id: int, db_session: AsyncSession):
    db_task = await get(todo_id, db_session)
    await db_session.delete(db_task)
    await db_session.commit()
