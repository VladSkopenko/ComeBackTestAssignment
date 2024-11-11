import logging

from src.core.exceptions import ErrorConnectingDb
from src.core.logging_config import get_logger
from src.core.messages import Messages
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

logger = get_logger(__name__)


async def check_postgres_connection(session: AsyncSession) -> ErrorConnectingDb:
    try:
        logger.info("Attempting to connect to PostgreSQL")
        result = await session.execute(select(1))
        logger.info("Successfully connected to PostgreSQL")
        return result.scalar() == 1
    except SQLAlchemyError as error:
        logger.error(f"Error connecting to PostgreSQL: {error}")
        raise ErrorConnectingDb(Messages.ERROR_CONNECTING_DATABASE)
    