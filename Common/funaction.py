# author:28487
# datetime:2019/12/16 18:57
# software: PyCharm

"""
文件说明：获取项目路径，测试系统的URL方法
"""

import os,configparser

def project_path():
    """
     获取项目路径
    :return:
    """

    return os.path.split(os.path.realpath(__file__))[0].split('C')[0]

def config_url():
    """
    返回config.ini文件中的testUrl
    :return:
    """
    config = configparser.ConfigParser()
    config.read(project_path()+"config.ini")
    return config.get('testUrl','url')


if __name__ == '__main__':
    print("项目路径为： "+project_path())
    print("被测系统URL为："+config_url())