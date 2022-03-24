from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router

def get_application() -> FastAPI:

    application = FastAPI()

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(api_router, prefix="/api/v1")
    return application


app = get_application()