# author:28487
# datetime:2019/12/16 22:29
# software: PyCharm

"""
文件说明：车票订单界面
"""
from Base.base import Base
from selenium.webdriver.common.by import By
import time


class OrderPage(Base):
    def passenger_name(self):
        """
        填写乘客姓名处
        :return:
        """
        return self.findele(By.XPATH, "//*[@id='pasglistdiv']/div/ul/li[2]/input")

    def passenger_cardnumber(self):
        """
        填写乘客证件号码处
        :return:
        """
        return self.findele(By.XPATH, "//*[@id='pasglistdiv']/div/ul/li[3]/input")

    def input_userinfo(self, username, cardnumber):
        """
        填写乘客的姓名和证件号码
        :param username: 乘客姓名
        :param cardnumber: 乘客证件号码
        :return:
        """
        time.sleep(2)
        self.passenger_name().send_keys(username)
        self.passenger_cardnumber().send_keys(cardnumber)
