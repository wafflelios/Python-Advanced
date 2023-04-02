from utils import calculator
import logging

logger = logging.getLogger('app')
logging.basicConfig(level=logging.DEBUG)

logger.info('The program has started.')
logger.warning("Don't forget that you can't divide by zero!")
num_1, operation, num_2 = input('Enter each character separated by space: ').split()
num_1, num_2 = int(num_1), int(num_2)
calculator(num_1, num_2, operation)
logger.info('App finished work.')
