from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from app.api.v1.endpoints.fileUpload import router as fileUploadRouter
from app.api.v1.endpoints.search import router as searchRouter




api_router = APIRouter()

@api_router.get("/")

async def read():
    return RedirectResponse('/docs')


api_router.include_router(fileUploadRouter, prefix="/fileUpload", tags=["fileUpload"])

api_router.include_router(searchRouter, prefix="/search", tags=["search"])