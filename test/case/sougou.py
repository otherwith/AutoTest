# author:28487
# datetime:2019/12/12 22:05
# software: PyCharm

"""
文件说明：
"""

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH


class TestBaiDu(unittest.TestCase):
    URL = Config().get('sougouURL')


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_search_0(self):
        self.driver.find_element_by_xpath("//*[@id='query']").send_keys("selenium")
        self.driver.find_element_by_xpath("//*[@id='stb']").click()
        time.sleep(5)
        self.assertEqual(self.driver.find_element_by_xpath("//*[@id='promotion_adv_container']/div/div/div/h3/a").is_displayed(),True,"搜索结果展示")



if __name__ == '__main__':
    unittest.main()