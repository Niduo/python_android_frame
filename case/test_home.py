# -*- coding: utf-8 -*-
"""
by: 老屋
"""
from appium import webdriver
from page.homePage import HomePage
import pytest

class TestRun:
    caps = {"deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "platformName": "Android"}
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def setup(self):
        self.driver.implicitly_wait(10)
        self.homePage = HomePage(self.driver)
        # update cancel
        # self.driver.find_element(By.ID, "image_cancel").click()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip("skip test")
    def test_search_ibm(self):
        self.homePage.search_stock()
        act = float(self.homePage.search_stock_result())
        assert act > 100, "ibm当前股票价格是：%s<100" % act

    def test_home_swift(self):
        self.homePage.swipe_home()
        act = self.homePage.swipe_home_result()
        assert act == "热门话题", "act, %s, 不等于热门话题" % act

