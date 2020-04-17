# -*- coding: utf-8 -*-
"""
by: 老屋
"""
from appium.webdriver import webdriver
from common import isElementExist
from page.basePage import BasePage
from common import saveImg
import sys
import logging


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('test_homePage...')


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver: webdriver = driver

    def search_stock(self):
        """
        des: 搜索ibm股票进入股票详情页
        :return:
        """
        if isElementExist.by_id_(self.driver, "image_cancel"):
            self.by_id("image_cancel").click()
            log.debug('image_cancel元素已定位到')
        else:
            log.debug('元素不存在')
        # 首页点击搜索框
        self.by_id("tv_search").click
        # 搜索ibm
        self.by_id("search_input_text").send_keys("ibm")
        # 选择第一个
        self.by_id("name").click()
        # 进入股票详情页
        self.by_id("stock_layout").click()

    def search_stock_result(self):
        """
        des: 获取ibm股票价格
        :return:
        """
        res = self.by_id("stock_current_price").text
        return res

    def swipe_home(self):
        """
        des: 首页向上向下分别滑动三次，测试拖动是否可用
        :return:
        """
        if isElementExist.by_id_(self.driver, "image_cancel"):
            self.by_id("image_cancel").click()
            # 切换到热门标签
            self.by_xpath("//android.widget.TextView[@text='热门']").click()
            log.debug('image_cancel元素已定位到')
        else:
            log.debug('更新弹窗元素不存在')
        self.by_id("com.xueqiu.android:id/title_text")
        size = self.get_screen_size()
        for i in range(3):
            self.driver.swipe(size['width']*0.5, size['height']*0.8,
                              size['width']*0.5, size['height']*0.3,
                              1500)
        for j in range(3):
            self.driver.swipe(size['width']*0.5, size['height']*0.3,
                              size['width']*0.5, size['height']*0.8,
                              1500)

    def swipe_home_result(self):
        """
        des: 获取热门话题文本
        :return:
        """
        if isElementExist.by_id_(self.driver, "hot_topic_tv"):
            res = self.by_id("hot_topic_tv").get_attribute("text")
            log.debug("get text: " + res)
            return res
        else:
            currentMethod = format(sys._getframe().f_code.co_name)
            saveImg.save_img(self.driver, currentMethod)
            log.debug("未找到元素")






