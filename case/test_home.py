# -*- coding: utf-8 -*-
"""
by: 老屋
"""
from appium import webdriver
from page.homePage import HomePage
from page.searchPage import SearchPage
from common import xmlRead
import pytest
import logging

logging.basicConfig(level='debug')
log = logging.getLogger('test home ...')


class TestRun:
    def setup_class(self):
        caps = {"deviceName": "127.0.0.1:7555",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "noReset": "true",
                "platformName": "Android"}
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        self.homePage = HomePage(self.driver)
        self.searchPage = SearchPage(self.driver)

    def teardown_class(self):
        print("end")
        self.driver.quit()

    a = ['ibm', 'jd']

    @pytest.mark.parametrize("key", a)
    def test_search_001(self, key):
        """
        des: 读取a列表数据分别在首页进行搜索
        :param key: 列表中轮循每一个元素
        :return:
        """
        try:
            exp = xmlRead.xml_read("case1", "result1")
            self.homePage.search().search_stock(key)
            act = float(self.searchPage.get_price())
            assert act > float(exp)
        except AssertionError as e:
            log.debug("断言失败", "当前股票价格是：%s<期望价格 %s" % (act, exp))
        # 返回首页
        finally:
            self.homePage.stock_detail_to_home()

    @pytest.mark.swipe
    def test_hot_swipe_002(self):
        """
        des: 热门标签页面上下滑动3次
        :return:
        """
        exp = xmlRead.xml_read("case2", "result")
        self.homePage.check_update_window()
        self.homePage.hot_label_up_down()
        act = self.homePage.get_hot_result()
        assert act == exp, "act, %s, 不等于热门话题%s" % (act, exp)

    @pytest.mark.skip("推荐标签上滑动")
    def test_recommended_swift_up_003(self):
        """
        des: 热门标签页面从下往上滑动3次
        :return:
        """
        self.homePage.recommended_label_up()
        act = self.homePage.get_recommended_up_res()
        assert act is True, "没有定位到结果"

    @pytest.mark.b
    def test_recommended_swift_down_004(self):
        """
        des: 热门标签页面从上往下滑动3次
        :return:
        """
        exp = xmlRead.xml_read("case4", "result")
        self.homePage.recommended_label_down()
        act = self.homePage.get_recommended_down_res()
        assert act == exp, "定位的是:%s 而不是%s" % (act, exp)



