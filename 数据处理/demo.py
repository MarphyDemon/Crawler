#getData
# import random

# def getData():
#     Data = [];
#     for i in range(0,100):
#         obj = {};
#         obj['id'] = i;
#         obj['value'] = i + random.randint(1,9);
#         Data.append(obj);
#     return Data;

# data = getData();
# print(data)
import codecs
import matplotlib.pyplot as pyl
from datetime import datetime
import numpy as np
import time


Data = []
def getData():  #此函数的作用主要是方便我们在getResult中获取数据内容通过数组的方式获得时间
    with codecs.open('shuju.csv', 'rb', 'gb2312') as csvfile:
        for i,line in enumerate(csvfile):  #循环csv数据
            obj = {};   #声明空的对象用于保存单条记录   obj:{key : 1, value: "具体的值，包含时间车牌等一系列内容"}
            if i > 0:   #i = 0时为表头  因此i>0去掉表头
                obj['key'] = i;     #将序号存入   
                obj['value'] = line;    #将内容存入   
                Data.append(obj);    #将单条记录插入数组
    return Data;
getData()#执行函数获取Data
# print(Data[29]);

# print(Data[35]);
# res = 0
def getResult(i,a): #此函数主要用于获取连续时间不大于10的end 即末尾序号  
    global n    #声明全局变量n，由于在下面我们给n赋值，并且要return末尾序号
    if i<a-2:   #判断i当前的值  是否超过Data数组长度
        # 此处主要用于取到i+1与i两个序号所对应的时间戳，通过Data[i]获取记录['value']获取前面赋给value的内容值（包含时间车牌等），
        #   split函数通过逗号分开所有的记录为一个数组，时间在[62231185,沪A09041D,2018\7\5 星期四 5:08:45，121.541904]中下标为2，
        #   此时获取到时间为'2018\7\5 星期四 5:08:45'通过空格切割字符串成['2018\7\5','星期四','5:08:45'],
        #   获取上面数组的日期和时间拼成新的时间字符串，‘2018\7\5 5:08:45’
        #此时获取到startTime与endTime
        endTime = Data[i+1]['value'].split(',')[2].split(" ")[0] + " " + Data[i+1]['value'].split(',')[2].split(" ")[2];
        startTime = Data[i]['value'].split(',')[2].split(" ")[0] + " " + Data[i]['value'].split(',')[2].split(" ")[2];
        # print(time.mktime(time.strptime(endTime,"%Y\%m\%d %H:%M:%S")),time.mktime(time.strptime(startTime,"%Y\%m\%d %H:%M:%S")))
        # print(time.mktime(time.strptime(endTime,"%Y\%m\%d %H:%M:%S"))-time.mktime(time.strptime(startTime,"%Y\%m\%d %H:%M:%S")))

        #   此处将时间字符串转为时间戳进行比较
        if (time.mktime(time.strptime(endTime,"%Y\%m\%d %H:%M:%S"))-time.mktime(time.strptime(startTime,"%Y\%m\%d %H:%M:%S")))<10.0:
            res = i+1;      #如果满足条件  对i+1
            getResult(res,a)    #如果满足i+1的时间比i的时间大20   则继续i+1继续调用函数本身继续判断 否则退出本函数保留res即end
        else:
            n = i;      #不满足条件时，获得末尾节点
    return n;       #return 末尾节点

start = 0
def doGetResult():
    arr = []        #声明数组用于存放最终我们的结果
    a = len(Data);  #获取Data数组长度
    end = getResult(start,a);   #第一次从0开始   
    if end-start >=3:   #获取末尾接点看是否相差最少三个相连，如果是插入arr
        arr.append([start,end])
    # print(end,a)
    while end<a-3:  #用于判断是否数组循环完成，如果end小于a-3，继续循环，>a-3说明整个数据Data循环完  
        #此处用于阻止数组陷入死循环，为啥这样写，经过测试应该是a-3时数组停止的  所以这样判断 ，具体可以在下面打印出end，看看，后议
        # print(s)
        s=end+1;    #此处用于给start重新赋值，第一次从0开始，执行完之后，我们给末尾节点加1，从下一个往后开始判断
        end = getResult(s,a);   #继续执行获取末尾节点函数
        if end-s >=3:
            arr.append([s+2,end+2])#获取末尾接点看是否相差最少三个相连，如果是插入arr
        # if end-start >=3:
        #     print(start,end)

        #     arr.append([start,end]);
    print(arr);#打印数组

doGetResult();#调用函数
