from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Optional
from uuid import UUID

from sqlalchemy import delete
from sqlalchemy import func
from sqlalchemy import insert
from sqlalchemy import RowMapping
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.exceptions import AddRecordError
from src.core.exceptions import NotFound
from src.core.messages import Messages


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict) -> RowMapping:
        raise NotImplementedError

    @abstractmethod
    async def find_all(
        self, skip: Optional[int], limit: Optional[int], **filter_by
    ) -> List[RowMapping]:
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, **filter_by) -> RowMapping:
        raise NotImplementedError

    @abstractmethod
    async def find_one_or_none(self, **filter_by) -> Optional[RowMapping]:
        raise NotImplementedError

    @abstractmethod
    async def edit_one(self, id: int, data: dict, **filter_by) -> RowMapping:
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, id: int) -> RowMapping:
        raise NotImplementedError

    @abstractmethod
    async def delete_many(self, **filters) -> None:
        raise NotImplementedError

    @abstractmethod
    async def count_all(self, **filter_by) -> int:
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> RowMapping:
        stmt = (
            insert(self.model).values(**data).returning(*self.model.__table__.columns)
        )
        res = await self.session.execute(stmt)
        result = res.fetchone()
        if result is None:
            raise AddRecordError(Messages.FILLED_TO_ADD_ERROR)
        return result._mapping

    async def edit_one(self, _id: UUID, data: dict, **filter_by) -> RowMapping:
        stmt = (
            update(self.model)
            .values(**data)
            .filter_by(id=_id, **filter_by)
            .returning(*self.model.__table__.columns)
        )
        res = await self.session.execute(stmt)
        result = res.fetchone()
        if result is None:
            raise NotFound(Messages.NOT_FOUND)
        return result._mapping

    async def find_all(
        self, skip: Optional[int] = None, limit: Optional[int] = None, **filter_by
    ):
        stmt = select(self.model).filter_by(**filter_by)
        if skip is not None:
            stmt = stmt.offset(skip)
        if limit is not None:
            stmt = stmt.limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def find_one(self, **filter_by) -> RowMapping:
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        return res.scalar_one()  # This will raise NoResultFound if no result

    async def find_one_or_none(self, **filter_by) -> Optional[RowMapping]:
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def delete_one(self, _id: UUID, **filter_by) -> RowMapping:
        stmt = (
            delete(self.model)
            .filter_by(id=_id, **filter_by)
            .returning(*self.model.__table__.columns)
        )
        res = await self.session.execute(stmt)
        result = res.fetchone()
        if result is None:
            raise NotFound(Messages.NOT_FOUND)
        return result._mapping

    async def delete_many(self, **filters) -> None:
        stmt = delete(self.model).filter_by(**filters)
        await self.session.execute(stmt)

    async def count_all(self, **filter_by) -> int:
        stmt = select(func.count()).select_from(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        return res.scalar()
