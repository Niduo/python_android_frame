# -*- coding: utf-8 -*-
"""
by: 老屋
"""
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webdriver import WebDriver
from common import isElementExist, saveImg
from page.basePage import BasePage
from page.searchPage import SearchPage
import logging
import time
import sys

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s)")
log = logging.getLogger(__name__)


class StockSelectPage(BasePage):
    currentMethod = format(sys._getframe().f_code.co_name)

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def add_stock(self, code):
        self.by_id("action_search").click()
        SearchPage(self.driver).search_stock(code)
        time.sleep(2)
        self.by_xpath("//*[@text='加自选']").click()
        log.debug("点击加自选")
        return self

    def get_stock_name(self):
        try:
            return [e.text for e in self.driver.find_elements(By.ID, 'portfolio_stockName')]
        except Exception as e:
            print(e)
            saveImg.save_img(self.driver, self.currentMethod)

    def is_add_popup(self, code):
        # toast = (By.XPATH, "//*[@test='添加成功']")
        # pop_windows = (By.XPATH, "//*[@text='下次再说']")
        # self.wait(pop_windows)
        # 判断是否首个参数
        if code == "jd":
            self.by_xpath("//*[@text='下次再说']").click()
            log.debug("有弹窗点击确认")
            self.driver.press_keycode(4)
            log.debug("点击一次返回搜索")
            time.sleep(2)
            self.driver.press_keycode(4)
            log.debug("再次点击返回行情页面")
        # 无弹窗按返回会到自选列表
        else:
            self.driver.press_keycode(4)
            time.sleep(2)
            self.driver.press_keycode(4)
            log.debug("无任何提示，返回行情页面")

    def clear_all(self):
        all = (By.XPATH, "//*[contains(@resource-id, 'indicator')]//*[@text='全部']")
        log.debug("定义需要等待的元素查找")
        self.wait(all)
        log.debug("wait完成")
        self.by_id("edit_group").click()
        log.debug("进入编辑group界面")
        if len(self.driver.find_elements(By.ID, "stockName")) > 0:
            self.by_xpath("//*[@text='全选']").click()
            log.debug("点击全选")
            self.by_xpath("//*[@text='取消关注']").click()
            log.debug("取消关注")
            self.by_id("tv_right").click()
            log.debug("点击确认")
            self.by_id("action_close").click()
        else:
            log.debug("列表为空")
            self.by_id("action_close").click()








