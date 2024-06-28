from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from typing import List
from pydantic import BaseModel
from app.services_model import batchsrv
from app.schema.batch import Batch
from app.exception.exception_handler import request_validation_exception_handler, http_exception_handler, \
    unhandled_exception_handler
import datetime

from app.config import logConf

logger = logConf.logload()
app = FastAPI(
    responses={404: {"description": "Not found bal bla"}},
)
app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

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


@router.post('/batchpayload/', tags=['Batch'], response_model=List[Batch], status_code=200)
async def batchpayload(batch: batchList):
    # return JSONResponse(status_code=200, content=batchsrv.batchpayload(batch))
    try:
        return JSONResponse(status_code=200, content=batchsrv.batchpayload(batch))
    except Exception as e:
        logger.exception(e)
    raise HTTPException(status_code=500, detail="Internal server error")

