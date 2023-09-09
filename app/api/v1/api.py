from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from app.api.v1.endpoints.fileUpload import router as fileUpload
from app.api.v1.endpoints.search import router as search




api_router = APIRouter()

@api_router.get("/")

async def read():
    return RedirectResponse('/docs')


api_router.include_router(fileUpload, prefix="/fileUpload", tags=["fileUpload"])

api_router.include_router(search, prefix="/search", tags=["search"])