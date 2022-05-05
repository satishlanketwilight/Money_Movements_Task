import logging
import os
import time
from logging.handlers import RotatingFileHandler


logged_on = time.strftime("%d%m%Y")
os_name = os.name
LOG_FILE_PATH = os.path.dirname(os.path.abspath(__file__))


LOG_FILENAME = "\\money_movements" + logged_on + ".log"
LOG_FILE = LOG_FILE_PATH + LOG_FILENAME


LOG_LVL = "INFO"

logger = logging.getLogger("money_movements")
logger.setLevel(logging.DEBUG)

fh = RotatingFileHandler(LOG_FILE, maxBytes=1000000, backupCount=5)

if LOG_LVL == "INFO":
    fh.setLevel(logging.INFO)

elif LOG_LVL == "WARNING":
    fh.setLevel(logging.WARN)

elif LOG_LVL == "DEBUG":
    fh.setLevel(logging.DEBUG)

elif LOG_LVL == "ERROR":
    fh.setLevel(logging.ERROR)

elif LOG_LVL == "CRITICAL":
    fh.setLevel(logging.CRITICAL)

formatter = logging.Formatter(
    "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s -> %(message)s"
)

fh.setFormatter(formatter)
logger.addHandler(fh)

# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')
