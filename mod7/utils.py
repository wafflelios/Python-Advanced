import logging

logger = logging.getLogger('calculator')
logging.basicConfig(level=logging.DEBUG)


def calculator(num_1, num_2, operation):
    logger.info('Calculator started working.')
    if operation in ['+', '-', '/', '//', '%', '*', '^']:
        try:
            if operation == '+':
                print(num_1 + num_2)
                logger.info('Summation completed successfully.')
            elif operation == '-':
                print(num_1 - num_2)
                logger.info('Subtraction completed successfully.')
            elif operation == '*':
                print(num_1 * num_2)
                logger.info('Multiplication completed successfully.')
            elif operation == '/':
                print(num_1 / num_2)
                logger.info('Division completed successfully.')
            elif operation == '//':
                print(num_1 // num_2)
                logger.info('Integer division completed successfully.')
            elif operation == '%':
                print(num_1 % num_2)
                logger.info('Division with remainder completed successfully.')
            else:
                print(pow(num_1, num_2))
                logger.info('Raising a number to a power completed successfully.')
        except ZeroDivisionError:
            print("Error: you can't divide by zero!")
            logger.error("Error: you can't divide by zero!")
    else:
        print('Error: unexpected operation.')
        logger.error('Error: unexpected operation.')
    logger.info('Calculator finished work.')