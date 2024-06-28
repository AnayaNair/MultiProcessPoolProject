from datetime import datetime
from multiprocessing import Pool
from app.config import logConf

logger = logConf.logload()
def f(x):
    sum = 0
    for i in x:
        try:
            sum = sum + i
        except ValueError:
            print('invalid input')

    return sum



def batchpayload(payload):
    now = datetime.now()
    payloadarr = []
    batchid = ""
    # print(payload[0][0])
    for row in payload:
        result = []
        if(row[0] == "payload" ):
            try:
                with Pool() as p:
                    result = p.map(f, row[1])
            except Exception:
                print('Unable to get the result')
        else:
            batchid = str(row[0])

    payloadarr.append({"batchid": batchid, "response": result, "status": "Complete", "started_at": str(now), "completed_at": str(now)})
    logger.info('Batch Executed successfully at:' +  str(now))
    return payloadarr