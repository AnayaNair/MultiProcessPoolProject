import time
import pytest
from app.endpoints_controller.batchfile import get_age
from app.endpoints_controller.batchfile import batchpayload
from app.endpoints_controller.batchfile import multiply



def test_batchpayloadpositive():
    # Given.
    res = {
        "batchid": "id101",
        "payload": [[2, 2], [3, 4]]
    }
    # When.
    result = batchpayload(res)
    # Then.
    assert result


def test_batchpayloadnegative():
    # Given.
    res = {
        "batchid": "id202",
        "payload": [[-2, 2], [3, 4]]
    }
    # When.
    result = batchpayload(res)
    # Then.
    assert result

