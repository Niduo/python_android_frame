# -*- coding: utf-8 -*-
"""
by: 老屋
"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def by_id(self, value):
        return self.driver.find_element(By.ID, value)

    def by_xpath(self, value):
        return self.driver.find_element(By.XPATH, value)

    def by_link(self, value):
        return self.driver.find_element(By.LINK_TEXT, value)

    def get_screen_size(self):
        return self.driver.get_window_size()

    def wait(self, locator, timeout=20):
        wt = WebDriverWait(self.driver, timeout)
        # 找到传入的所有元素
        if isinstance(locator, tuple):
            wt.until(lambda x: len(self.driver.find_elements(*locator)) > 0)
        elif isinstance(locator, str):
            wt.until(lambda x: locator in self.driver.page_source)
        # 找到其中一个值即可
        elif isinstance(locator, list):
            def wait_list(driver: WebDriver):
                source = driver.page_source
                return any(map(lambda x: x in source, locator))
            wt.until(wait_list)
        else:
            print("不知道如何去识别这个元素{locator}")

    def open_wait(self, locator):
        wt = WebDriverWait(self.driver, timeout=5)
        flag = False
        try:
            wt.until(self.driver.find_element(locator))
            return True
        except NoSuchElementException as e:
            print("该元素等待5s后未找到", e)
            return flag

    def exception_handle(fun):
        def magic(*args, **kwargs):
            instance: BasePage = args[0]
            try:
                result = fun(*args, **kwargs)
                instance.retry = 0
                return result
            except Exception as e:
                instance.retry += 1
                if instance.retry > instance._retry_max:
                    raise e
                instance.driver.implicitly_wait(0)
                for e in instance.black_list:
                    elements = instance.driver.find_element(*e)
                    if len(elements) > 0:
                        elements[0].click()
                        instance.driver.implicitly_wait(10)
                        return fun(*args, **kwargs)
        return magic




