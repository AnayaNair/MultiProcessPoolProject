import uvicorn
import time
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from app.routers.api import router as api_router

app = FastAPI()

origins = [
    "*",
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


if __name__ == '__main__':
    uvicorn.run("main:app", host='', port=8000, log_level="info", reload=True)
    print("running")


