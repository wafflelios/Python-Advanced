from custom_level_handler import LayeredHandler
import sys
from ASCII_only import ASCIIFilter

dict_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'ASCIIFilter': {
            '()': ASCIIFilter
        }
    },
    'formatters': {
        'base': {
            'format': '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'base',
            'stream': sys.stdout
        },
        'file': {
            '()': LayeredHandler,
            'level': 'DEBUG',
            'formatter': 'base'
        },
        'time_rotating': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/utils.log',
            'when': 'h',
            'interval': 10,
            'backupCount': 5,
            'level': 'INFO',
            'formatter': 'base'
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'filters': ['ASCIIFilter']
        },
        'utils_logger': {
            'level': 'DEBUG',
            'handlers': ['console', 'file', 'time_rotating'],
            'filters': ['ASCIIFilter']
        }
    }
}