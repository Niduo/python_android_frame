# -*- coding: utf-8 -*-
"""
by: 老屋
"""
from selenium.webdriver.common.by import By


def by_id_(driver, value):
    flag = True
    try:
        driver.find_element(By.ID, value)
        return flag
    except:
        flag = False
        return flag