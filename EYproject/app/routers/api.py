import time
from fastapi import APIRouter, FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from app.endpoints_controller import batchfile
origins = [
    "*",
    "http://localhost",
    "http://127.0.0.1",
"http://localhost:8000",
]
router = APIRouter()
app = FastAPI()
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

router.include_router(batchfile.router)