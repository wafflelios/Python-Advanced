import logging


class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        if '"' in msg:
            msg = msg.replace('"', "'")
        return msg, kwargs


logger = JsonAdapter(logging.getLogger())

logging.basicConfig(level=logging.DEBUG, filename='skillbox_json_messages.log',
                    format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}',
                    datefmt='%H:%M:%S')

logger.info('"hello"')