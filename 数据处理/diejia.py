import pandas as pda
import numpy as np
import matplotlib.pyplot as pyl
import matplotlib.font_manager

question = 'question.xlsx'
data = pda.read_excel(question,'Sheet1')
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
    minuteList = getMinute()
    result = getMinuteData(data[ind.min():ind.max()],minuteList)
    return result

def getMinute():
    minuteList = []
    for i in range(0,24):
        for j in range(0,60):
            if j<10:
                minute = "0"+str(j)
            else:
                minute = str(j)
            minuteList.append([str(i),minute])
    return minuteList

def getMinuteData(dateData,minuteList):
    result = []
    for (hour,minute) in minuteList:
        count = 0
        for j in dateData['小时']:
            dataArrList = str(j).split(":")
            if hour==dataArrList[0] and minute==dataArrList[1]:
                count = count+1
        result.append(count)
    return result


def main():
    answer_date = getDate()
    print(answer_date)
    series = getDayData(answer_date[0])
    series1 = getDayData(answer_date[1])
    series2 = getDayData(answer_date[2])
    series3 = getDayData(answer_date[3])
    series4 = getDayData(answer_date[4])
    series5 = getDayData(answer_date[5])
    series6 = getDayData(answer_date[6])
    x = np.linspace(0, 24, 6)
    pyl.xlim(0, 24)
    pyl.plot(series,'F069235-',series1,'F120650-',series2,'F233800-',series3,'F184700-',series4,'F365030-',series5,'F839000-',series6,'black-')
    # 
    pyl.show()

main()