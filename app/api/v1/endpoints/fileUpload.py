from typing import Any
from fastapi import APIRouter, BackgroundTasks, UploadFile
from fastapi.responses import JSONResponse
from uuid import uuid4

from app.utils.textExtraction.main import textExtraction
from app.utils.vectorTransformer.main import VectorTransformer
from app.db.main import Database

router = APIRouter()


@router.post("/")
async def Upload(
    background_tasks: BackgroundTasks,
    file: UploadFile
) -> Any:
    try:
        responseTextExtraction=textExtraction().Text(await file.read())
        background_tasks.add_task(file.file.close)

        totalstr=""
        for i in responseTextExtraction:
            totalstr+= " "+i[0]

        responseVectorTransformer=VectorTransformer().transform(totalstr)
        data={
            "id":str(uuid4()),
            "values":responseVectorTransformer.tolist(),
            "metadata":{
                "filename":file.filename,
                "content_type":file.content_type,
                "text_extraction":totalstr,
            }
        }
        Database().insert(indexName="risetech",data=data)
        return JSONResponse(content={"detail": "success"}, status_code=200)



    except Exception as e:
        return JSONResponse(content={"detail": str(e)}, status_code=400)
