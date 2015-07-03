# -*- coding: utf-8 -*-

import os
import logging
from logging import StreamHandler
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# log level
ERROR = logging.ERROR
WARNING = logging.WARNING
INFO = logging.INFO
DEBUG = logging.DEBUG

# handler_type
ROTATING_FILE = 'rotating_file'
TIMED_ROTATING_FILE = 'timed_rotating_file'

LOG_DIR = './log'
LOG_CATEGORY_DIR_NAME = 'MOCAL'
LOG_FILE_NAME = 'mocal.log'


def get_log_handler(log_path, handler_type):
    handlers = {
        'rotating_file': RotatingFileHandler(log_path, maxBytes=10*1024*1024, backupCount=5),  # 最多备份5个日志文件，每个文件10M
        'timed_rotating_file': TimedRotatingFileHandler(log_path, 'D', 1, 30)
    }

    return handlers[handler_type]

LOG_FORMAT = '[%(asctime)s][%(levelname)s][%(name)s]%(message)s -- %(filename)s line:%(lineno)d'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


class Logger:
    def __init__(self, log_name='mocal', log_category_dir=LOG_CATEGORY_DIR_NAME, log_file_name=LOG_FILE_NAME,
            log_level=INFO, log_format=LOG_FORMAT, handler_type=TIMED_ROTATING_FILE, datefmt=DATE_FORMAT):

        self.log = logging.getLogger(log_name)
        self.log.setLevel(log_level)
        self.formatter = logging.Formatter(log_format, datefmt)

        self.log_path = os.path.join(LOG_DIR, log_category_dir, log_file_name)
        if not os.path.exists(os.path.dirname(self.log_path)):
            os.makedirs(os.path.dirname(self.log_path))

        # init handlers
        # default log handler
        s_handler = StreamHandler()
        s_handler.setLevel(log_level)
        s_handler.setFormatter(self.formatter)
        self.log.addHandler(s_handler)

        self.handler = get_log_handler(self.log_path, handler_type)
        self.handler.setLevel(log_level)
        self.handler.setFormatter(self.formatter)

        self.log.addHandler(self.handler)

    def info(self, msg):
        self.log.info(msg)

    def error(self, msg):
        self.log.error(msg)

    def debug(self, msg):
        self.log.debug(msg)

    def warning(self, msg):
        self.log.warning(msg)

    def rename(self, name):
        self.log.name = name

logger = Logger('mocal')

