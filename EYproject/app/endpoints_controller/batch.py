from fastapi import APIRouter, FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse, JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from typing import List
from app.services_model import batchsrv
from app.schema.batch import Batch
from pydantic import BaseModel
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from app.config import logConf
logger = logConf.logload()

# APIRouter creates path operations for user module
router = APIRouter(
    prefix="/batch",
    tags=["Batch"],
    responses={404: {"description": "Not found"}},
)
app = FastAPI()

class batchList(BaseModel):
  batchid: str
  payload: List[List[int]]


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
   return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return await request_validation_exception_handler(request, exc)



@router.post('/batchpayload/', tags=['Batch'], response_model=List[Batch], status_code=200)
async def batchpayload(batch: batchList):
    # return JSONResponse(status_code=200, content=batchsrv.batchpayload(batch))
    try:
        return JSONResponse(status_code=200, content=batchsrv.batchpayload(batch))
    except Exception as e:
        logger.exception(e)
    raise HTTPException(status_code=500, detail="Internal server error")



