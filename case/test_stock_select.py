# -*- coding: utf-8 -*-
"""
by: 老屋
"""

from appium import webdriver
from page.homePage import HomePage
from page.stockSelectPage import StockSelectPage
import pytest
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


class TestStockSelect:
    def setup_class(self):
        caps = {"deviceName": "127.0.0.1:7555",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "platformName": "Android"}
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        self.homePage = HomePage(self.driver)
        self.stockPage = StockSelectPage(self.driver)

    def teardown_class(self):
        self.driver.quit()
        log.debug("class end...........")

    # stockChnName = ["京东", "IBM Corp", "拼多多"]
    # stockEngName = ["jd", "ibm", "pdd"]
    # parameter = [(stockChnName, stockEngName)]

    @pytest.mark.parametrize('name, code', [("京东", "jd"), ("IBM Corp", "ibm"), ("拼多多", "pdd")])
    def test_add_stock(self, name, code):
        """
        des: 搜索股票加入到自选列表
        :param key: 列表中轮循每一个元素
        :return:
        """
        self.homePage.stock_page().add_stock(code).is_add_popup(code)
        act = self.stockPage.get_stock_name()
        print("name:", type(name), name)
        print("name:", type(act), act)
        assert name in act, "股票名称不正确,返回名称是%s, 期望值是%s" % (act, name)

    # @pytest.mark.skip("skip")
    def test_clear_stock(self):
        self.homePage.stock_page().clear_all()
        assert "京东" not in self.driver.page_source, "股票未成功取消"
        assert "IBM" not in self.driver.page_source, "股票未成功取消"
        assert "拼多多" not in self.driver.page_source, "股票未成功取消"

