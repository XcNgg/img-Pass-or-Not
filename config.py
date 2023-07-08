import datetime
from loguru import logger

# todo
# 百度接口配置,需要官网申请
APP_ID = ""
API_KEY = ""
SECRET_KEY =""


logger.add(
    f"./log/{datetime.datetime.now().strftime('%Y-%m-%d')}.log",
    rotation="100 MB",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | [{level}] | {module}:{function}:{line} - {message}",
    colorize=True
)