from Logger.log import logging
import pandas

def func(x,y):
    try:
        return x/y
    except Exception as e:
        logging.info(e)

func(3/4)