# -*- coding: utf-8 -*-
"""
by: 老屋
"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from page.basePage import BasePage
from common import saveImg
import logging
import sys

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s)")
log = logging.getLogger(__name__)


class SearchPage(BasePage):
    currentMethod = format(sys._getframe().f_code.co_name)

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def search_stock(self, key_words):
        """
        des: 搜索ibm股票进入股票详情页
        :return:
        """
        try:
            self.by_id("search_input_text").send_keys(key_words)
            log.debug("搜索关键字%s" % key_words)
            # 选择第一个
            self.by_id("name").click()
            log.debug("点击第一个候选结果")
            # 进入股票详情页
            self.by_id("stock_layout").click()
            log.debug("进入股票详情")
        except NoSuchElementException as e:
            log.debug("未找到元素", e)
            saveImg.save_img(self.driver, self.currentMethod)
        return self

    def get_price(self):
        """
        des: 获取ibm股票价格
        :return:
        """
        try:
            res = self.by_id("stock_current_price").text
            log.debug("获取股票价格")
            return res
        except NoSuchElementException as e:
            log.debug("未找到元素")
            saveImg.save_img(self.driver, self.currentMethod)