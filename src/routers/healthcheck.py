from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.exceptions import ErrorConnectingDb
from src.core.logging_config import get_logger
from src.core.messages import Messages
from src.db.database import get_session
from src.db.postgres_db import check_postgres_connection

logger = get_logger(__name__)

router = APIRouter(
    prefix="/health",
    tags=["Health check"],
)


@router.get("")
async def health_check():
    logger.info("Health check endpoint was called")
    return {"status_code": 200, "detail": "ok", "result": "working"}


@router.get("/postgres")
async def health_check_postgres(session: AsyncSession = Depends(get_session)):
    postgres_status = await check_postgres_connection(session)
    if postgres_status:
        logger.info("Successfully connected to PostgreSQL")
        return {"postgresql": "connected"}
    else:
        logger.error("Error connecting to PostgreSQL")
        raise ErrorConnectingDb(Messages.ERROR_CONNECTING_DATABASE)
