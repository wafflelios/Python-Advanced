from utils import calculator
import logging.config
from logging_config import dict_config
import logging

logging.config.dictConfig(dict_config)
app_logger = logging.getLogger('app_logger')
'''
form = '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s'
formatter = logging.Formatter(fmt=form)
logging.basicConfig(level=logging.DEBUG, format=form, stream=sys.stdout)
app_logger = logging.getLogger('app_logger')
level_handler = LayeredHandler()
level_handler.setFormatter(formatter)
app_logger.addHandler(level_handler)
'''
app_logger.info('The program has started.')
app_logger.warning("Don't forget that you can't divide by zero!")
num_1, operation, num_2 = input('Enter each character separated by space: ').split()
num_1, num_2 = int(num_1), int(num_2)
calculator(num_1, num_2, operation)
app_logger.info('App finished work.')