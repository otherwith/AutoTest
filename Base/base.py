# author:28487
# datetime:2019/12/16 21:17
# software: PyCharm

"""
文件说明：项目中涉及的底层操作
"""
from Common.log import FrameLog
from selenium import webdriver


# 对base代码进行优化、增加
class Base():
    def __init__(self, driver):
        self.driver = webdriver.Chrome()
        self.log = FrameLog().log()

    # 单星号表示此处接受任意多个非关键字参数
    def findele(self, *args):
        """
        定位元素
        :param args:
        :return:
        """
        try:
            print(args)
            self.log.info("通过" + args[0] + "定位，元素是" + args[1])
            return self.driver.find_element(*args)
        except:
            # 页面上没有定位到相应的元素
            self.log.error("定位元素失败！")

    def click(self, args):
        """
        对元素click
        :param args:
        :return:
        """
        self.findele(args).click()

    def sendkey(self, args, value):
        """
        输入值
        :param args:
        :param value:
        :return:
        """
        self.findele(args).send_keys(value)

    def js(self, str):
        """
        调用js方法
        :param str:
        :return:
        """
        self.driver.execute_script(str)

    def url(self):
        """
        获取当前页面的url
        :return:
        """
        return self.driver.current_url

    def back(self):
        """
        后退操作
        :return:
        """
        self.driver.back()

    def forword(self):
        """
        前进操作
        :return:
        """
        self.driver.forward()

    def quit(self):
        """
        退出浏览器操作
        :return:
        """
        self.driver.quit()
