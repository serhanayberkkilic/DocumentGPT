from typing import Any
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse



router = APIRouter()



@router.get("/")

def read(
) -> Any:

    try:
        result="Hello World"
        return result

    except Exception as e:
        return JSONResponse(content={"detail":str(e)},status_code=400)