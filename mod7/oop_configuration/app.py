from utils import calculator
import sys
import logging

form = '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s'
logging.basicConfig(level=logging.DEBUG, format=form, stream=sys.stdout)
app_logger = logging.getLogger('app_logger')

app_logger.info('The program has started.')
app_logger.warning("Don't forget that you can't divide by zero!")
num_1, operation, num_2 = input('Enter each character separated by space: ').split()
num_1, num_2 = int(num_1), int(num_2)
calculator(num_1, num_2, operation)
app_logger.info('App finished work.')
