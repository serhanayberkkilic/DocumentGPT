from typing import Any
from fastapi import APIRouter, BackgroundTasks, UploadFile
from fastapi.responses import JSONResponse

from app.utils.textExtraction.main import textExtraction


router = APIRouter()


@router.post("/")
async def Upload(
    background_tasks: BackgroundTasks,
    file: UploadFile
) -> Any:
    try:
        responseTextExtraction=textExtraction().Text(await file.read())
        background_tasks.add_task(file.file.close)

        print(responseTextExtraction)



    except Exception as e:
        return JSONResponse(content={"detail": str(e)}, status_code=400)
