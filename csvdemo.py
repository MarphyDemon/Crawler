# import csv
# csvfile = open('cap1.csv',newline='')#打开一个文件
# csvReader = csv.reader(csvfile)#返回的可迭代类型
# print(type(csvReader))
# for cont in csvReader:
#   print(cont)
# csvfile.close()#关闭文件

# import csv
# with open('cap1.csv', mode='rb') as f:
#     reader = csv.reader(f)
# for i, rows in enumerate(csvReader):
#     try:
#         row1 = [row1.decode('GB2312').encode('utf-8') for row1 in rows]
#     except:
#         row1 = [row1.decode('GBK').encode('utf-8') for row1 in rows]

import codecs
import matplotlib.pyplot as pyl

onerow=[]
tworow=[]
with codecs.open('cap1.csv', 'rb', 'gb2312') as csvfile:
    for i,line in enumerate(csvfile):
        if i==1:
            print(line)
            print(list(line.strip().split(',')))
            onerow = list(line.strip().split(','))
            for j in onerow:
                print(j)
        if i==2:
            print(line)
            print(list(line.strip().split(',')))
            tworow = list(line.strip().split(','))
            for k in onerow:
                print(k)


    l1, = pyl.plot(onerow, label = '', color = 'yellow', linewidth = 1.0, linestyle = '',marker='o')
    l2, = pyl.plot(tworow, label = '', color = 'tan', linewidth = 1.0, linestyle = '',marker='o')
    pyl.legend(handles = [l1,l2], labels = ['one','two'], loc = 'upper right') 
    pyl.show()




