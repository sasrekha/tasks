import logging

logging.basicConfig(filename="logs.txt", filemode="a", format="%(asctime)s : %(filename)s : %(funcName)s : %(levelname)s : %(lineno)d : %(message)s")
logger = logging.getLogger()

logger.setLevel(logging.INFO)
logger.info("Something to log")
logger.setLevel(logging.DEBUG)
logger.debug("Debugging an issue")

try:
    l = [1,2,3]
    print(l[4])
    x,y = 1,0
    a = x/y
    
except IndexError as ie:
    logger.setLevel(logging.ERROR)
    logger.exception(ie)
except ZeroDivisionError as e:
    logger.setLevel(logging.ERROR)
    logger.exception(e)
