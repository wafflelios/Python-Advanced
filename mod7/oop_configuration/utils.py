import logging

utils_logger = logging.getLogger('calculator')


def calculator(num_1, num_2, operation):
    utils_logger.info('Calculator started working.')
    if operation in ['+', '-', '/', '//', '%', '*', '^']:
        try:
            if operation == '+':
                utils_logger.debug(f'Result: {num_1 + num_2}')
                utils_logger.info('Summation completed successfully.')
            elif operation == '-':
                utils_logger.debug(f'Result: {num_1 - num_2}')
                utils_logger.info('Subtraction completed successfully.')
            elif operation == '*':
                utils_logger.debug(f'Result: {num_1 * num_2}')
                utils_logger.info('Multiplication completed successfully.')
            elif operation == '/':
                utils_logger.debug(f'Result: {num_1 / num_2}')
                utils_logger.info('Division completed successfully.')
            elif operation == '//':
                utils_logger.debug(f'Result: {num_1 // num_2}')
                utils_logger.info('Integer division completed successfully.')
            elif operation == '%':
                utils_logger.debug(f'Result: {num_1 % num_2}')
                utils_logger.info('Division with remainder completed successfully.')
            else:
                utils_logger.debug(f'Result: {pow(num_1, num_2)}')
                utils_logger.info('Raising a number to a power completed successfully.')
        except ZeroDivisionError:
            utils_logger.error("Error: you can't divide by zero!")
    else:
        utils_logger.error('Error: unexpected operation.')
    utils_logger.info('Calculator finished work.')
