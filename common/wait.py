# -*- coding: utf-8 -*-
"""
by: 老屋
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from common import isElementExist
from page.basePage import BasePage
from page.homePage import HomePage
import time
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('test_homePage...')


class M:
    # def __init__(self):
    #     caps = {"deviceName": "127.0.0.1:7555",
    #             "appPackage": "com.xueqiu.android",
    #             "appActivity": ".view.WelcomeActivityAlias",
    #             "platformName": "Android"}
    #     self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    #     self.driver.implicitly_wait(10)

    def waita(self, locate, timeout=20):
        wt = WebDriverWait(self.driver, timeout)
        # 找到传入的所有元素
        if isinstance(locate, tuple):
            wt.until(lambda x: len(self.driver.find_element(*locate)) > 0)
        elif isinstance(locate, str):
            wt.until(lambda x: locate in self.driver.page_source)
        # 找到其中一个值即可
        elif isinstance(locate, list):
            def wait_list(driver: WebDriver):
                source = driver.page_source
                return any(map(lambda x : x in source, locate))
            wt.until(wait_list)

    def hom(self):
        # BasePage(self.driver).wait(["王炸", "邬炼"])
        if isElementExist.by_id_(self.driver, "image_cancel"):
            self.by_id("image_cancel").click()
            log.debug('image_cancel元素已定位到')
        else:
            log.debug('更新元素不存在')
        try:
            a = (By.ID, "tv_search")
            self.click(a)
        except Exception as e:
            log.debug("异常.......................")
            self.driver.press_keycode(4)
            print("ddddddddddddddddddddddddddddddddddddddddddddddddddd")

    def if_(self):
        if 2 % 0 == 0:
            print("0/2")
        else:
            print("error....")


stockChnName = ["京东", "IBM Corp", "拼多多"]
stockEngName = ["jd", "ibm", "pdd"]
parameter = [(stockChnName, stockEngName)]


print(parameter)
print(stockEngName)
print(parameter[0][1][0])


# m = M()
# m.if_()