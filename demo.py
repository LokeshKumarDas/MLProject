from MLProject.logger import logging
from MLProject.exception import Exception
import sys

logging.info('this is custom log')

try:
    a =2/0 # get 0 division exception
    
except Exception as e:
    raise Exception(e, sys)