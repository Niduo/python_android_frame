# -*- coding: utf-8 -*-
"""
by: 老屋
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver


class BasePage:
    def __init__(self, driver):
        self.driver: webdriver = driver

    def by_id(self, value):
        return self.driver.find_element(By.ID, value)

    def by_xpath(self, value):
        return self.driver.find_element(By.XPATH, value)

    def by_link(self, value):
        return self.driver.find_element(By.LINK_TEXT, value)

    def get_screen_size(self):
        return self.driver.get_window_size()
