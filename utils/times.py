#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import datetime
from functools import wraps

# 规范化时间便于复用


def timestamp():
    """时间戳"""
    return time.time()


def datetime_strftime(fmt="%Y%m"):
    """datetime格式化时间"""
    return datetime.datetime.now().strftime(fmt)


def sleep(seconds=1.0):
    """
    睡眠时间
    """
    time.sleep(seconds)


def run_time(func):
    """运行时长"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = timestamp()
        res = func(*args, **kwargs)
        print("Done！用时%.3f秒！" % (timestamp() - start_time))
        return res

    return wrapper


if __name__ == '__main__':
    print(timestamp())
