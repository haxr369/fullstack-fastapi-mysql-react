from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from api.api_v1.api import api_router
from core.config import settings

app = FastAPI()

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        #disallow_unlisted_origins =True
    )

"""origins = [
    "http://172.28.0.3:3005",
    "http://172.28.0.3",
    "http://192.168.0.203:3005/"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)"""

app.include_router(api_router, prefix=settings.API_V1_STR)
@app.get("/")
async def root():
    return {"message": "/plant 에서 사용자관리"}


