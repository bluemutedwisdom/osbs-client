import  logging

def set_logging(name="osbs", level=logging.DEBUG):
    # create logger
    logger = logging.getLogger(name)
    logger.handlers = []
    logger.setLevel(level)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)


set_logging(level=logging.WARNING)  # override this however you want
