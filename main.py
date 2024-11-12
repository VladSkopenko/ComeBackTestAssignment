import threading

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.staticfiles import StaticFiles

from src.core.config import settings
from src.core.logging_config import get_logger
from src.routers.dependencies import DocumentWordServiceDep
from src.routers.dependencies import UOWDep
from src.routers.document_word import router as document_word_router
from src.routers.healthcheck import router as health_check_router
from src.utils.open_browser import open_browser

logger = get_logger(__name__)

app = FastAPI(title="ComeBack-API-Service")

app.mount("/static", StaticFiles(directory="src/static"), name="static")

templates = Jinja2Templates(directory="src/static/templates")

app.add_middleware(
    CORSMiddleware,  # Cross-Origin Resource Sharing !!!!!!!!!!!!!
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/formatted", response_class=HTMLResponse)
async def all_documents_page(request: Request, document_service: DocumentWordServiceDep,
                             uow: UOWDep, ):
    documents_list = await document_service.get_all_document_word(uow=uow, limit=10, )
    return templates.TemplateResponse("formatted.html", {"request": request, "documents": documents_list})


app.include_router(document_word_router)
app.include_router(health_check_router)

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)
