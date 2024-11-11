from abc import ABC
from abc import abstractmethod

from src.db.database import async_session
from src.repositories.document_word import DocumentWordRepository


class IUnitOfWork(ABC):
    """
    Interface for UnitOfWork pattern, which ensures atomicity of database operations.
    This interface is designed to handle multiple repositories in a single transaction.
    """

    documents: DocumentWordRepository

    @abstractmethod
    def __init__(self):
        """
        Initialize the UnitOfWork.
        """
        pass

    @abstractmethod
    async def __aenter__(self):
        """
        Enter the runtime context related to this object.
        This method is called when the execution flow enters the context of the 'async with' statement.
        """
        pass

    @abstractmethod
    async def __aexit__(self, *args):
        """
        Exit the runtime context related to this object.
        This method is called when the execution flow leaves the context of the 'async with' statement.
        """
        pass

    @abstractmethod
    async def commit(self):
        """
        Commit the transaction.
        This method is used to save the changes made during the UnitOfWork.
        """
        pass

    @abstractmethod
    async def rollback(self):
        """
        Rollback the transaction.
        This method is used to undo the changes made during the UnitOfWork in case of an error.
        """
        pass


class UnitOfWork(IUnitOfWork):
    """
    Concrete implementation of the UnitOfWork interface.
    Manages database transactions and ensures all changes are committed or rolled back atomically.
    """

    def __init__(self):
        """
        Initialize the UnitOfWork with an asynchronous session factory.
        """
        self.session_factory = async_session

    async def __aenter__(self):
        """
        Initialize the asynchronous database session and repositories.
        Called when entering the 'async with' context.
        """
        self.session = self.session_factory()
        self.documents = DocumentWordRepository(self.session)

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Commit or rollback the transaction based on whether an exception occurred.
        Close the asynchronous database session.
        """
        if exc_type is not None:
            await self.rollback()
        else:
            await self.commit()
        await self.session.close()
        if exc_type is not None:
            raise exc_val.with_traceback(
                exc_tb
            )

    async def commit(self):
        """
        Commit the transaction.
        Save all changes made during the UnitOfWork.
        This is an asynchronous operation.
        """
        await self.session.commit()

    async def rollback(self):
        """
        Rollback the transaction.
        Undo all changes made during the UnitOfWork.
        This is an asynchronous operation.
        """
        await self.session.rollback()
