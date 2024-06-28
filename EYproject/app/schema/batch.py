from pydantic import BaseModel

class Batch(BaseModel):
    batchid: str
    payload: str
    response: str
    status: str
    started_at: str
    completed_at: str
