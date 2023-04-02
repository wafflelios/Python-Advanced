import logging_tree.format

from utils import calculator
from logging_tree import printout
import logging.config
from logging_config import dict_config
import logging

logging.config.dictConfig(dict_config)
app_logger = logging.getLogger('app_logger')

app_logger.info('The program has started.')
app_logger.warning("Don't forget that you can't divide by zero!")
num_1, operation, num_2 = input('Enter each character separated by space: ').split()
num_1, num_2 = int(num_1), int(num_2)
calculator(num_1, num_2, operation)
app_logger.info('App finished work.')

with open('logging_tree.txt', 'w') as file:
    file.write(logging_tree.format.build_description())