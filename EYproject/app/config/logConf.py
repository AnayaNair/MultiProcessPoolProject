import logging



def logload():

    uvicorn_access = logging.getLogger("uvicorn.access")
    uvicorn_access.disabled = True

    logger = logging.getLogger("uvicorn")
    logger.setLevel(logging.getLevelName(logging.DEBUG))

    # define file handler and set formatter
    file_handler = logging.FileHandler('event_related.log')
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    file_handler.setFormatter(formatter)

    # add file handler to logger
    logger.addHandler(file_handler)


    return logger

