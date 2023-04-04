import logging
import string


class ASCIIFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        # или просто:
        # return record.msg.isascii()
        # но просили написать свое
        flag = True
        for letter in record.msg:
            if letter not in string.printable:
                flag = False
                break
        return flag
