from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse


from app.api.v1 import api
from app.core.config import settings



app = FastAPI(
    title=settings.projectName,
    description=settings.projectDescription,
    terms_of_service=settings.termsOfService
)

# Set all CORS enabled origins
if settings.backendCorsOrigins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.backendCorsOrigins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


from starlette.requests import Request
from starlette.responses import Response

async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception:
        return Response("Internal server error", status_code=500)

app.middleware('http')(catch_exceptions_middleware)




@app.get("/")
async def root():
    return RedirectResponse('/docs')


############Router#################
app.include_router(api.api_router, prefix=settings.apiStr)