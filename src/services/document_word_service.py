import logging
from uuid import UUID

from src.core.exceptions import NotFound
from src.core.logging_config import get_logger
from src.core.messages import Messages
from src.utils.unitofwork import IUnitOfWork


logger = get_logger(__name__)


class DocumentWordService:
    """
    Service for managing documents word.
    """

    @staticmethod
    async def get_document_word_by_id(
            uow: IUnitOfWork, document_word_id: UUID
    ):
        async with uow:
            organization = await uow.documents.find_one_or_none(
                id=document_word_id
            )
            if organization is None:
                raise NotFound(Messages.NOT_FOUND)
            return organization

    @staticmethod
    async def update_document_word_by_id(
            uow: IUnitOfWork, document_word_id: UUID

    ):
        async with uow:
            document_word_updated = await uow.documents.edit_one(
                document_word_id, data={"active": False} # todo доробити
            )

            return document_word_updated

    @staticmethod
    async def delete_organization_by_id(
            uow: IUnitOfWork, document_word_id: UUID
    ) -> None:
        async with uow:
            await uow.documents.delete_one(document_word_id)
