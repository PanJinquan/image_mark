# -*- coding: utf-8 -*-
from numpy import *


#保存txt数据
def save_txt(content,filename,mode='a'):
    """保存txt数据
    :param content:需要保存的数据
    :param filename:文件名
    :param mode:读写模式
    :return: void
    """
    file = open(filename,mode)
    for row in range(len(content)):
        for col in content[row]:
            file.write(str(col)+' ')
        file.write( '\n')
    file.close()

#读取txt数据函数
def read_txt(fileName):
    """读取txt数据函数
    :param filename:文件名
    :return: txt的数据列表
    :rtype: list
    """
    Data=[]
    with open(fileName) as txtData:
        lines=txtData.readlines()
        for line in lines:
            lineData=line.strip()#去除空白和逗号“,”
            Data.append(lineData)
    return Data

#按空格分割字符串，并以列表的形式返回
def splitData(dataSet):
    """分割字符串
    :param dataSet:文件名
    :return: 按空格分割字符串，并以列表的形式返回
    :rtype: list
    """
    re=[]
    for str in dataSet:
        str_list = str.split()
        int_list=[]
        for i in str_list:
            if i.isdigit():
                int_list.append(int(i))
            else:
                int_list.append(i)
        re.append(int_list)
    return re

if __name__ == '__main__':
    # test_text = ['1.jpg','dog',200,300]
    test_text= [['1.jpg', 'dog', 200, 300], ['2.jpg', 'dog', 20, 30]]
    save_txt(test_text,'test.txt',mode='w')
    data=read_txt('test.txt')
    print(data)
    data=splitData(data)
    print(data)
    print(data)



