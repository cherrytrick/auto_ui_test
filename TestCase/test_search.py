#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import unittest
from selenium import webdriver

from utils.logger import Logger
from common.readconfig import ini
from page_object.searchpage import SearchPage
# from chromedriver_py import binary_path

log = Logger(__name__).logger


class TestSearch(unittest.TestCase):
    """搜索测试"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.search = SearchPage(cls.driver)
        cls.search.get_url(ini.url)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        self.imgs = []

    def test_001(self):
        """搜索"""
        self.search.input_search("selenium")
        self.search.click_search()
        result = re.search(r'selenium', self.search.get_source)
        log.info(result)
        assert result

    def test_002(self):
        """测试搜索候选"""
        self.search.input_search("selenium")
        log.info(list(self.search.imagine))
        assert all(["selenium" in i for i in self.search.imagine])


if __name__ == '__main__':
    unittest.main(verbosity=2)
