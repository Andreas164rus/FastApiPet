from app.crud.base import CRUDBase
from app.models.task import Task
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class TaskCRUDBase(CRUDBase):


    async def get_by_status(
        self,
        status: str,
        session: AsyncSession,
        user_id: int
    ) -> list[Task]:
        tasks_db = await session.execute(
                select(Task).where(
                    Task.status == status,
                    Task.user_id == user_id
                )
        )
        return tasks_db.scalars().all()

task_crud = TaskCRUDBase(Task)