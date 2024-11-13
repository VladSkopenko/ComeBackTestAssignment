from functools import wraps
from typing import Callable
from uuid import UUID

from fastapi import UploadFile

from src.core.exceptions import BadRequest
from src.core.exceptions import InvalidCredentials
from src.core.exceptions import NotFound
from src.core.messages import Messages
from src.utils.unitofwork import IUnitOfWork


def document_check(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(
        uow: IUnitOfWork, document_word_id: UUID, *args, **kwargs
    ):
        if not isinstance(document_word_id, UUID):
            raise InvalidCredentials(Messages.NOT_VALIDATE)

        async with uow:

            document_word = await uow.documents.find_one_or_none(id=document_word_id)
            if document_word is None:
                raise NotFound(Messages.NOT_FOUND)


            return await func(uow, document_word_id, document_word, *args, **kwargs)

    return wrapper


def validate_extension(*extensions):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, file: UploadFile, **kwargs):
            if not any(file.filename.endswith(ext) for ext in extensions):
                raise BadRequest(f"Дозволені тільки файли з розширеннями: {', '.join(extensions)}."
                                 )
            return await func(*args, file=file, **kwargs)

        return wrapper

    return decorator
