from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from src.routers.dependencies import DocumentWordServiceDep
from src.routers.dependencies import UOWDep

router = APIRouter()
templates = Jinja2Templates(directory="src/static/templates")


@router.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/formatted", response_class=HTMLResponse)
async def all_documents_page(request: Request, document_service: DocumentWordServiceDep,
                             uow: UOWDep, ):
    documents_list = await document_service.get_all_document_word(uow=uow, limit=10, )
    return templates.TemplateResponse("formatted.html", {"request": request, "documents": documents_list})
