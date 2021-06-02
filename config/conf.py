#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from selenium.webdriver.common.by import By
from utils.times import datetime_strftime


class ConfigManager(object):
    # 项目目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 配置文件
    INI_PATH = os.path.join(BASE_DIR, 'config', 'config.ini')

    # 页面元素目录
    ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')

    # 报告目录
    REPORT_PATH = os.path.join(BASE_DIR, 'report')

    # 测试用例
    TEST_SUITES = os.path.join(BASE_DIR, "TestCase")

    # 元素定位的类型
    LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class': By.CLASS_NAME
    }

    # 邮件信息
    EMAIL_INFO = {
        'username': '3534058330@qq.com',  # 切换成你自己的地址
        'password': 'QQ邮箱授权码',
        'smtp_host': 'smtp.qq.com',
        'smtp_port': 465
    }

    # 收件人
    ADDRESSEE = ['3534058330@qq.com', ]

    @property
    def log_path(self):
        # 日志目录
        log_path = os.path.join(self.BASE_DIR, 'logs')
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        return os.path.join(log_path, '{}.log'.format(datetime_strftime()))

    @property
    def report_path(self):
        """报告文件"""
        _path = self.REPORT_PATH
        if not os.path.exists(_path):
            os.makedirs(_path)
        return os.path.join(_path, '{}.html'.format(datetime_strftime("%Y%m%d_%H%M%S")))

    @property
    def get_new_report(self):
        """获取最新的报告"""
        _path = self.REPORT_PATH
        report_path = os.listdir(_path)
        report_new_path = sorted(report_path,
                                 key=lambda x: os.path.getmtime(os.path.join(_path, x)))
        report_new_file = os.path.join(_path, report_new_path[-1])
        with open(report_new_file, encoding='utf-8') as f:
            return f.read()


cm = ConfigManager()
if __name__ == '__main__':
    print(cm.BASE_DIR)
