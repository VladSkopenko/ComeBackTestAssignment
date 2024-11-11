from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from src.core.config import settings
from src.core.exceptions import ErrorConnectingDb
from src.core.logging_config import get_logger
from src.core.messages import Messages

logger = get_logger(__name__)
engine = create_async_engine(str(settings.db.url), echo=True, future=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_session() -> AsyncSession:
    """
    Provides an asynchronous database session.

    This function is used for healthcheck endpoint for Postgres

    Yields:
        AsyncSession: The database session.

    Raises:
        SQLAlchemyError: If an error occurs during the session, it is logged and the transaction is rolled back.
    """
    async with async_session() as session:
        try:
            logger.info("Session started")
            yield session
            await session.commit()
            logger.info("Session committed")
        except SQLAlchemyError as error:
            await session.rollback()
            logger.error(f"Session rollback due to: {error}")
            raise ErrorConnectingDb(Messages.ERROR_CONNECTING_DATABASE)
