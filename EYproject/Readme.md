EYProject MultiProcessing Pool:

    This project is created to implement addition on input lists of integers using 
        Python's multiprocessing pool in FastAPI

Request Format:
{
        "batchid": "string",
        "payload": [[2, 2], [3, 4]]
}

	
Response body:
[
  {
    "batchid": "batchid",
    "response": [
      4,
      7
    ],
    "status": "Complete",
    "started_at": "2024-06-28 08:56:13.025236",
    "completed_at": "2024-06-28 08:56:13.025236"
  }
]

Installation:
    pip install pydantic
    pip install pytest


Main Execute:
    To run use uvicorn main:app --reload

Execute test case:
    pytest -vs app/tests/tests_batchfile.py
