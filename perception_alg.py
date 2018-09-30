
import numpy as np

def loadDataSet(fileName):
    data = []
    label = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        data.append([lineArr[0],lineArr[1]])
        label.append(lineArr[2])
    return data,label

#给出了导入数据的代码
#请实现今天上课的感知器算法
#并输出结果
#可以利用numpy库
#建议编译环境pycharm
