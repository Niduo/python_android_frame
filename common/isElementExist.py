# -*- coding: utf-8 -*-
"""
by: 老屋
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


def by_id_(driver, value):
    flag = True
    try:
        driver.find_element(By.ID, value)
        return flag
    except Exception as e:
        flag = False
        return flag


def by_xpath_(driver, value):
    flag = True
    try:
        driver.find_element(By.XPATH, value)
        return flag
    except Exception as e:
        flag = False
        return flag


def by_id_elements_(driver, value):
    flag = True
    try:
        driver.find_elements(By.ID, *value)
        return flag
    except Exception as e:
        flag = False
        return flag
