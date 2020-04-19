# -*- coding: utf-8 -*-
"""
by: 老屋
"""
from appium.webdriver import webdriver
from common import isElementExist
from page.basePage import BasePage
from page.searchPage import SearchPage
from page.stockSelectPage import StockSelectPage
from common import saveImg
import sys
import logging
import time


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s)")
log = logging.getLogger(__name__)


class HomePage(BasePage):
    currentMethod = format(sys._getframe().f_code.co_name)

    def __init__(self, driver):
        self.driver: webdriver = driver
        self.size = self.get_screen_size()

    def search(self):
        """
        des: 搜索股票进入股票详情页
        :return:
        """
        if isElementExist.by_id_(self.driver, "image_cancel"):
            self.by_id("image_cancel").click()
            log.debug('image_cancel元素已定位到并点击去除弹窗')
        else:
            log.debug('更新弹窗不存在')
        # 首页点击搜索框
        self.by_id("tv_search").click()
        log.debug("点击首页搜索框")
        return SearchPage(self.driver)

    def stock_page(self):
        """
        des: 点击行情进入自选股票界面
        :return:
        """
        if isElementExist.by_id_(self.driver, "image_cancel"):
            self.by_id("image_cancel").click()
            log.debug('image_cancel元素已定位到')
        else:
            log.debug('更新元素不存在')
        self.by_xpath("//*[@text='行情']").click()
        log.debug('进入行情')
        return StockSelectPage(self.driver)

    def stock_detail_to_home(self):
        """
        des: 在详情页返回首页
        :return:
        """
        self.driver.press_keycode(4)
        time.sleep(2)
        self.driver.press_keycode(4)
        time.sleep(1)

    def check_update_window(self):
        """
        des 点击需求更新窗口的弹窗
        :return:
        """
        if isElementExist.by_id_(self.driver, "image_cancel"):
            self.by_id("image_cancel").click()
            log.debug('image_cancel元素已定位到')
        else:
            log.debug('更新弹窗元素不存在')

    def hot_label_up_down(self):
        """
        des: 热门标签页面上下滑动3次
        :return:
        """
        self.by_xpath("//android.widget.TextView[@text='热门']").click()
        self.swipe_up()
        self.swipe_down()

    def get_hot_result(self):
        """
        des: 获取热门话题文本
        :return:
        """
        if isElementExist.by_id_(self.driver, "hot_topic_tv"):
            res = self.by_id("hot_topic_tv").get_attribute("text")
            log.debug("get text: " + res)
            return res
        else:
            saveImg.save_img(self.driver, self.currentMethod)
            log.debug("未找到元素截图")

    def recommended_label_down(self):
        """
        des: 推荐标签从上往下滑动3次
        :return:
        """
        self.by_xpath("//android.widget.TextView[@text='推荐']").click()
        self.swipe_down()

    def get_recommended_down_res(self):
        """
        des: 定位"推荐"文本并返回
        :return:
        """
        if isElementExist.by_xpath_(self.driver, "//android.widget.TextView[@text='推荐']"):
            res = self.by_xpath("//android.widget.TextView[@text='推荐']").text
            return res
        else:
            saveImg.save_img(self.driver, self.currentMethod)
            log.debug("未找到元素截图")

    def recommended_label_up(self):
        """
        des: 推荐标签从下到上滑动3次
        :return:
        """
        self.by_xpath("//android.widget.TextView[@text='推荐']").click()
        self.swipe_up()

    def get_recommended_up_res(self):
        """
        des: 推荐标签从上到下滑动3次定位是否有搜索框并返回
        :return:
        """
        return self.by_id("tv_search")

    def swipe_up(self):
        """
        des: 从下到上滑动3次
        :return:
        """
        for j in range(3):
            self.driver.swipe(self.size['width'] * 0.5, self.size['height'] * 0.8,
                              self.size['width'] * 0.5, self.size['height'] * 0.3,
                              1500)

    def swipe_down(self):
        """
        des: 从上到下滑动3次
        :return:
        """
        for j in range(3):
            self.driver.swipe(self.size['width'] * 0.5, self.size['height'] * 0.3,
                              self.size['width'] * 0.5, self.size['height'] * 0.8,
                              1500)
