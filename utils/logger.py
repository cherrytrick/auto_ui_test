#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import logging
from config.conf import cm


class Logger:
    def __init__(self, name=None):
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

            # 创建一个handle写入文件
            fh = logging.FileHandler(cm.log_path, encoding='utf-8')
            fh.setLevel(logging.INFO)

            # 创建一个handle输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 定义输出的格式
            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 添加到handle
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    @property
    def fmt(self):
        return '%(levelname)s\t%(asctime)s\t%(name)s:%(lineno)d\t%(message)s'


if __name__ == '__main__':
    log = Logger(__name__).logger
    log.info('hello world')
