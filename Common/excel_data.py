# author:28487
# datetime:2019/12/16 19:47
# software: PyCharm

"""
文件说明：处理测试数据文件（Excel）
"""
import xlrd, os


def read_excel(filename, index):
    """
    读excel操作，所有数据存放在字典中
    :param filename: 文件名
    :param index: Excel的sheet工作簿索引
    :return:
    """
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)
    print(sheet.nrows)
    print(sheet.ncols)
    dic = {}
    for j in range(sheet.ncols):
        data = []
        for i in range(sheet.nrows):
            data.append(sheet.row_values(i)[j])
        dic[j] = data

    return dic


if __name__ == '__main__':
    # 读取Excel操作，返回字典
    data = read_excel(os.path.split(os.path.realpath(__file__))[0].split('C')[0] + "Data\\testdata.xlsx", 0)
    print(data)
    print(data.get(1))
