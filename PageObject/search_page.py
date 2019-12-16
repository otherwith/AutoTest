# author:28487
# datetime:2019/12/16 21:46
# software: PyCharm

"""
文件说明：火车车次搜索界面
"""

from Base.base import Base
from selenium.webdriver.common.by import By
import time
class SearchPage(Base):
    def search_leave(self):
        """
        出发站
        :return:
        """
        return self.findele(By.ID,"notice01")

    def search_arrive(self):
        """
        到达站
        :return:
        """
        return self.findele(By.ID,"notice08")

    def search_data(self):
        """
        出发时间
        :return:
        """
        return self.findele(By.ID,"dateObj")

    def search_btn(self):
        """
        搜索按钮
        :return:
        """
        return self.findele(By.ID,"searchbtn")

    def search_current(self):
        """
        单程
        :return:
        """
        return self.findele(By.XPATH,"//*[@id='searchtype']/li[1]")

    def search_js(self,value):
        """
        js移除出发时间的“readonly”属性
        :param value:
        :return:
        """
        jsvalue = "document.getElementById('dateObj').value='%s'"%(value)
        self.js(value)

    def search_train(self,leave,arrive,leave_date):
        """
        根据出发城市、到达城市和出发日期搜索火车车次信息
        :param leave: 出发城市
        :param arrive: 到达城市
        :param leave_date: 出发日期
        :return:
        """
        self.search_leave().send_keys(leave)
        time.sleep(2)
        self.search_arrive().send_keys(arrive)
        self.search_js(leave_date)
        self.search_btn().click()
        time.sleep(4)
        # return self.url()