# author:28487
# datetime:2019/12/16 22:07
# software: PyCharm

"""
文件说明：火车票预订页面
"""
from Base.base import Base
from selenium.webdriver.common.by import By
import time


class BookPage(Base):
    def book_ticket(self, train_number):
        """
        通过车次定位该车次的二等座的预订按钮
        :param train_number: 车次（如：G307）
        :return:
        """
        return self.findele(By.XPATH, "//*[@booking='B" + train_number + "-209']")

    def book_typeD(self):
        """
        动车前的复选框
        :return:
        """
        return self.findele(By.XPATH, "//*[@class='checkbox' and @ubtm='车型|动车']")

    def book_btn(self, train_number):
        """
        实现点击目标动车的二等座的预约按钮
        :param train_number: 车次
        :return:
        """
        try:
            time.sleep(2)
            self.book_typeD().click()
            time.sleep(2)
            self.book_ticket(train_number).click()

        except:
            self.log.error("车次查询失败")
            None
        return self.url()
