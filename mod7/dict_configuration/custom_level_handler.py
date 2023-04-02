import logging


class LayeredHandler(logging.Handler):
    def __init__(self):
        super().__init__()

    def emit(self, record: logging.LogRecord) -> None:
        with open(f'logs/calc_{record.levelname.lower()}.log', 'a') as file:
            file.write(self.format(record) + '\n')
