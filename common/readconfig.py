#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import configparser
from config.conf import cm

HOST = 'HOST'


class ReadConfig:
    """配置文件"""

    def __init__(self):
        self.path = cm.INI_PATH
        if not os.path.exists(self.path):
            raise FileNotFoundError("配置文件%s不存在！" % self.path)
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(self.path, encoding='utf-8')

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(self.path, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST, HOST)


ini = ReadConfig()

if __name__ == '__main__':
    print(ini.url)
