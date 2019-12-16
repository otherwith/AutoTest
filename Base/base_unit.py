# author:28487
# datetime:2019/12/16 21:33
# software: PyCharm

"""
文件说明：抽离单元测试中的setUp和tearDown方法
"""
import unittest
from Common.funaction import config_url
from selenium import webdriver


# 抽离单元测试中的setUp和tearDown
class UnitBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get(config_url())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def tearDownClass(cls) -> None:
        cls.driver.quit()
