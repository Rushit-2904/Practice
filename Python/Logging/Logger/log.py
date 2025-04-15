import os
from datetime import datetime 
import logging

log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(logs_path)

log_file_path = os.path.join(logs_path,log_file)


logging.basicConfig(
    filename=log_file_path,
    level=logging.DEBUG,
    format=' %(name)s : %(asctime)s : %(levelname)s : %(message)s'
)




def func(x,y):
    try:
        return x/y
    except Exception as e:
        logging.info(e)

func(3,0)