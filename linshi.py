# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 09:10:11 2018

@author: Administrator
"""
0
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from datetime import datetime

df=pd.read_csv('shuju.csv',encoding='utf-8')
df['tempaver']=(df['tempmax']+df['tempmin'])/2

df1=df[(-1 <= df['current']) & (df['current'] <= 1)]
#print(df1['current'])
lstsoc=np.array(df1['soc'])
lstvolt=np.array(df1['voltage'])
lsttemp=np.array(df1['tempaver'])
st=np.array(df1['addTime'])
print(st)
#print(lstsoc)
#print(len(lstsoc))
soc=[]
volt=[]
tempaver=[] 
xu=[]
start=0
for i in range(100):
    t1=datetime.strptime(st[i],"%Y-%m-%d %H:%M:%S.000")
    t2=datetime.strptime(st[i+1],"%Y-%m-%d %H:%M:%S.000")
#    print((t2-t1).seconds)
    if (t2-t1).seconds > 15:
        end=i
    if end-start >=3:
        xu.append((start,end))
print(xu)
#         print(st[i])
#        for i in 
#        soc.append(lstsoc[i])
#        soc.append(lstsoc[i+1])
#        volt.append(lstvolt[i])
#        volt.append(lstvolt[i+1])
#        tempaver.append(lsttemp[i])
#        tempaver.append(lsttemp[i+1])
#print(soc)
#print(np.shape(soc))
    

#s1=time.strptime(st[0],"%Y-%m-%d %H:%M:%S.000")
#time1 = int(time.mktime(s1))
#s2=time.strptime(st[1],"%Y-%m-%d %H:%M:%S.000")
#time2 = int(time.mktime(s2))
#print(st[0])
#print(st[1])
#time1=datetime.strptime(st[0],"%Y-%m-%d %H:%M:%S.000")
#time2=datetime.strptime(st[1],"%Y-%m-%d %H:%M:%S.000")
#print((time2-time1).seconds)
#count=0
#for i in range(100):
#    time1=datetime.strptime(st[i],"%Y-%m-%d %H:%M:%S.000")
#    time2=datetime.strptime(st[i+1],"%Y-%m-%d %H:%M:%S.000")
#print((time2-time1).seconds)
#    t=(time2-time1).seconds
#    if t <=15:
#        count=count+1
#    print(count)
#if count >=2:
#    soc.append(lstsoc[i])
#    soc.append(lstsoc[i+1])
#    volt.append(lstvolt[i])
#    volt.append(lstvolt[i+1])
#    tempaver.append(lsttemp[i])
#    tempaver.append(lsttemp[i+1])
#print(soc)
