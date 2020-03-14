"""
Logging 模块主要记录日志的生成，包括运行过程中的命令输出，已经日志保存到文件

"""

import logging
from common.tools import root_dir
import os,sys

root = root_dir()
logs_path = os.path.join(root,'logs')
if not os.path.exists(logs_path):
    os.mkdir(logs_path)


class Log:

    __logger:logging.Logger = None

    def __new__(cls, *args, **kwargs):
        if cls.__logger is None:
            # 创建Loggr
            cls.__logger = logging.getLogger('cnodeApi')
            cls.__logger.setLevel(logging.DEBUG)

            fh = logging.FileHandler(logs_path+'/app.log')
            fh.setLevel(logging.DEBUG)

            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)

            formatter = logging.Formatter(' %(asctime)s [%(levelname)s] - %(name)s - %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            cls.__logger.addHandler(fh)
            cls.__logger.addHandler(ch)

        return cls.__logger


if __name__ == '__main__':
    log1 = Log()
    log2 = Log()

    print(log1 is log2)