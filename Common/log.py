# author:28487
# datetime:2019/12/16 19:22
# software: PyCharm

"""
文件说明:日志类
"""
import logging, time
from Common.funaction import project_path


class FrameLog():
    def __init__(self, logger=None):
        # 创建一个logger

        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        self.log_time = time.strftime("%Y%m%d%H%M%S_")
        # 路径需要修改
        self.log_path = project_path() + "/Logs/"
        self.log_name = self.log_path + self.log_time + 'log.log'
        print(self.log_name)
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '[%(asctime)s] $(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        # 在记录日志后移除句柄
        self.logger.removeHandler(fh)

        # 关闭打开的文件
        fh.close()

    def log(self):
        return self.logger


if __name__ == '__main__':
    lo = FrameLog()
    log = lo.log()
    log.error("error")
    log.debug("debug")
    log.info("info")
    log.critical("critical")
