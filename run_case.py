#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import unittest
from config.conf import cm
from utils.send_mail import send_report_mail
from utils.HTMLTestRunner_cn import HTMLTestRunner

discover = unittest.defaultTestLoader.discover(cm.TEST_SUITES, pattern="test*.py")


def main():
    """主函数"""
    try:
        with open(cm.report_path, 'wb+') as fp:
            runner = HTMLTestRunner(stream=fp,
                                    title="测试结果",
                                    description="用例执行情况",
                                    verbosity=2,
                                    retry=1,
                                    save_last_try=True)
            result = runner.run(discover)
    except Exception as e:
        print("用例执行失败:{}".format(e))
    else:
        if result.failure_count or result.error_count:
            # 如果测试有错误，就发送邮件
            send_report_mail()


if __name__ == "__main__":
    main()
