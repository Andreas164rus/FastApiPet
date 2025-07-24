from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.schemas.task import TaskCreate, TaskDB
from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.task import task_crud

router = APIRouter()


@router.post("/", response_model=TaskDB)
async def create_task(
    task: TaskCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    task = await task_crud.create(task, session)
    return task

@router.get("/{status}", response_model=list[TaskDB])
async def tasks_by_status(
    status: str,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    tasks = await task_crud.get_by_status(status, session)
    return tasks
    

@router.put("/{task_id}", response_model=TaskDB)
async def update_task(
    task_id: int,
    task_update: TaskCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    task = await task_crud.get(task_id, session)
    if task is None:
        raise HTTPException(status_code=404, detail="Задачи с таким id не существет!")
    if task.user_id != user.id:
        raise HTTPException(status_code=404, detail="Задачи с таким id не существет!")
    update_task = await task_crud.update(task, task_update, session)
    return update_task


@router.delete("/{task_id}")
async def delete_task(    
    task_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    task = await task_crud.get(task_id, session)
    if task is None:
        raise HTTPException(status_code=404, detail="Задачи с таким id не существет!")
    if task.user_id != user.id:
        raise HTTPException(status_code=404, detail="Задачи с таким id не существет!")
    deleted_task = await task_crud.remove(task, session)
    return deleted_task