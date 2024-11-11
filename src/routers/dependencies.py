from typing import Annotated

from fastapi import Depends

from src.services.document_word_service import DocumentWordService
from src.utils.unitofwork import IUnitOfWork
from src.utils.unitofwork import UnitOfWork


def get_uow() -> IUnitOfWork:
    return UnitOfWork()


def get_document_word_service() -> DocumentWordService:
    return DocumentWordService()


UOWDep = Annotated[IUnitOfWork, Depends(get_uow)]
DocumentWordServiceDep = Annotated[DocumentWordService, Depends(get_document_word_service)]
