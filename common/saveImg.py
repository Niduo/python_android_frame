# -*- coding: utf-8 -*-
"""
by: 老屋
"""
# from selenium.webdriver.remote.webdriver import WebDriver
import time
import os

nowTime = time.strftime('%y%m%d_%H%M%S', time.localtime())
current_path = __file__
# dadDir = os.path.abspath(os.path.join(current_path, os.pardir, os.pardir))
father = os.path.dirname(os.path.dirname(current_path))


def save_img(driver, method_name):
    filename = father + "/report/errorImg/" + method_name + "_" + nowTime +".png"
    driver.get_screenshot_as_file(filename)
