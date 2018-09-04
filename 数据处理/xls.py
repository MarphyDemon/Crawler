import pandas as pda
import numpy as np
import matplotlib.pyplot as pyl
from matplotlib.font_manager import FontProperties

font = FontProperties(fname='./wqy-zenhei.ttc')

# pyl.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签  
# pyl.rcParams['axes.unicode_minus'] = False #用来正常显示负号  
pyl.figure()  
question = 'question.xlsx'
data = pda.read_excel(question,'Sheet1')
# print(data)
row = data.shape[0]
col = data.shape[1]

def getDate():
    DateArr_set=set(data['日期'])
    answer_date = []
    for each in DateArr_set:
        if each not in answer_date:
            answer_date.append(each)
    return answer_date


def getDayData(dateStr):
    datestr = str(dateStr)[0:10]
    ind = data[data.日期==datestr].index
    # minuteList = getMinute()
    # print(ind.min(),ind.max())
    print(data[ind.min():ind.max()])
    result = getMinuteData(data[ind.min():ind.max()])
    return result

# def getMinute():
#     minuteList = []
#     for i in range(0,24):
#         for j in range(0,60):
#             if j<10:
#                 minute = "0"+str(j)
#             else:
#                 minute = str(j)
#             minuteList.append([str(i),minute])
#     return minuteList

def getMinuteData(dateData):
    result = []
    for hour in range(0,24):
        count = 0
        for j in dateData['时间']:
            if hour==int(j):
                count = count+1
        result.append(count)
        print(result)
    return result


def main():
    answer_date = getDate()
    print(answer_date[0],answer_date[1],answer_date[2],answer_date[3],answer_date[4],answer_date[5],answer_date[6])
    series = getDayData(answer_date[0])
    series1 = getDayData(answer_date[1])
    series2 = getDayData(answer_date[2])
    series3 = getDayData(answer_date[3])
    series4 = getDayData(answer_date[4])
    series5 = getDayData(answer_date[5])
    series6 = getDayData(answer_date[6])
    x = np.linspace(0, 25, 6)
    pyl.xlim(0, 25)
    pyl.title('香蜜湖路市委党校路段',fontproperties=font)
    pyl.xlabel('小时',fontproperties=font)
    pyl.ylabel('辆/小时',fontproperties=font)
    # pyl.plot(series,"r-",series1,'b-',series2,'g-',series3,'y-',series4,'p-',series5,'s-',series6,'c-')
    l1, = pyl.plot(series, label = 'line', color = 'blue', linewidth = 1.0, linestyle = '-')
    l2, = pyl.plot(series1, label = 'line', color = 'green', linewidth = 1.0, linestyle = '-')
    l3, = pyl.plot(series2, label = 'line', color = 'purple', linewidth = 1.0, linestyle = '-')
    l4, = pyl.plot(series3, label = 'line', color = 'red', linewidth = 1.0, linestyle = '-')
    l5, = pyl.plot(series4, label = 'line', color = 'yellow', linewidth = 1.0, linestyle = '-')
    l6, = pyl.plot(series5, label = 'line', color = 'tan', linewidth = 1.0, linestyle = '-')
    l7, = pyl.plot(series6, label = 'line', color = 'gray', linewidth = 1.0, linestyle = '-')
    # pyl.legend(loc='upper left') 
    pyl.legend(handles = [l1, l2,l3,l4,l5,l6,l7], labels = [str(answer_date[0])[5:10],str(answer_date[1])[5:10],str(answer_date[2])[5:10],str(answer_date[3])[5:10],str(answer_date[4])[5:10],str(answer_date[5])[5:10],str(answer_date[6])[5:10]], loc = 'upper right') 
    pyl.show()

main()