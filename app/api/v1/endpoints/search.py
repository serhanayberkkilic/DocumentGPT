from typing import Any
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse


from app.schemas import searchSchemas
from app.utils.vectorTransformer.main import VectorTransformer
from app.db.main import Database
from app.utils.azureOpenAI.main import ChatCompletionClass

router = APIRouter()



@router.post("/")

def send(
    search: searchSchemas.Create,
) -> Any:

    try:
        responseVectorTransformer=VectorTransformer().transform(search.text)
        response=Database().search(indexName="risetech",vector=responseVectorTransformer.tolist(),top_k=1)
        metadata = response["matches"][0]["metadata"]["text_extraction"]
        resp=ChatCompletionClass().QuestionAnswer(question=search.text,datas=metadata)
        return JSONResponse(content={"Answer":resp},status_code=200)



    except Exception as e:
        return JSONResponse(content={"detail":str(e)},status_code=400)