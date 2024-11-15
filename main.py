import threading

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from src.core.config import settings
from src.core.logging_config import get_logger
from src.routers.document_word import router as document_word_router
from src.routers.frontend import router as frontend_router
from src.routers.healthcheck import router as health_check_router
from src.utils.open_browser import open_browser

logger = get_logger(__name__)

app = FastAPI(title="ComeBack-API-Service")

app.mount("/static", StaticFiles(directory="src/static"), name="static")

templates = Jinja2Templates(directory="src/static/templates")

app.add_middleware(
    CORSMiddleware,  # Cross-Origin Resource Sharing !!!!!!!!!!!!!
    allow_origins=["localhost", "127.0.0.1"],
    allow_credentials=True,
    allow_methods=["Get", "Post", "Patch"],
    allow_headers=["*"],
)

app.include_router(frontend_router)
app.include_router(document_word_router)
app.include_router(health_check_router)

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)
