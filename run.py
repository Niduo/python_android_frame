# -*- coding: utf-8 -*-
"""
by: 老屋
des:雪球app测试demo
evn: jdk 1.8/ sdk / nodejs 10.13 / Appium desktop 1.8.2 / mumu virtual / xueqiu app

"""

import pytest
import os
import time

currentDir = __file__
father = os.path.dirname(currentDir)
nowTime = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
# case var
homePageCase = 'test_home_'

report_name = father + '/report/' + homePageCase + nowTime + '.html'

# home page
homePage = ['-v', './case/test_home.py', '--html='+report_name]

# mark swipe
swipe = ['-vm', 'swipe', '--html='+report_name]

# stock select
stockSelect = ['-v', './case/test_stock_select.py', '--html='+report_name]

if __name__ == '__main__':
    pytest.main(stockSelect)




