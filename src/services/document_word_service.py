from typing import Optional
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
    async def create_document_word(
            uow: IUnitOfWork, dropbox_path: str,
    ):
        async with uow:
            document_word = await uow.documents.add_one(data={"original_document": dropbox_path})
            return document_word

    @staticmethod
    async def get_document_word_by_id(
            uow: IUnitOfWork, document_word_id: UUID
    ):
        async with uow:
            document_word = await uow.documents.find_one_or_none(
                id=document_word_id
            )
            if document_word is None:
                raise NotFound(Messages.NOT_FOUND)
            return document_word

    @staticmethod
    async def update_document_word_by_id(
            uow: IUnitOfWork, document_word_id: UUID, data

    ):
        async with uow:
            document_word_updated = await uow.documents.edit_one(
                document_word_id, data={"formatted_apa": data}
            )

            return document_word_updated

    @staticmethod
    async def delete_document_word_by_id(
            uow: IUnitOfWork, document_word_id: UUID
    ) -> None:
        async with uow:
            await uow.documents.delete_one(document_word_id)

    @staticmethod
    async def get_all_document_word(
            uow: IUnitOfWork,
            limit: Optional[int] = None
    ):
        async with uow:
            document_word = await uow.documents.find_all(limit=limit)
            return document_word
