import logging

logger = logging.getLogger('calculator')
logging.basicConfig(level=logging.DEBUG)


def calculator(num_1, num_2, operation):
    logger.info('Calculator started working.')
    if operation in ['+', '-', '/', '//', '%', '*', '^']:
        try:
            if operation == '+':
                logger.debug(num_1 + num_2)
                logger.info('Summation completed successfully.')
            elif operation == '-':
                logger.debug(num_1 - num_2)
                logger.info('Subtraction completed successfully.')
            elif operation == '*':
                logger.debug(num_1 * num_2)
                logger.info('Multiplication completed successfully.')
            elif operation == '/':
                logger.debug(num_1 / num_2)
                logger.info('Division completed successfully.')
            elif operation == '//':
                logger.debug(num_1 // num_2)
                logger.info('Integer division completed successfully.')
            elif operation == '%':
                logger.debug(num_1 % num_2)
                logger.info('Division with remainder completed successfully.')
            else:
                logger.debug(pow(num_1, num_2))
                logger.info('Raising a number to a power completed successfully.')
        except ZeroDivisionError:
            logger.error("Error: you can't divide by zero!")
    else:
        logger.error('Error: unexpected operation.')
    logger.info('Calculator finished work.')
