from django.shortcuts import render
from django.http import JsonResponse
from django.db.models.functions import TruncDate
import pymysql
from backend.views import resp,sqlsetting
# Create your views here.
import logging
# Get an instance of a logger
logger = logging.getLogger('sourceDns.webdns.views')
# config={
#     "host":"127.0.0.1",
#     "user":"root",
#     "password":"marphy0817",
#     "database":"lagouone",
#     "charset":"utf8"
# }
def getSucCount():
    db = pymysql.connect(**sqlsetting.con())
    cursor = db.cursor()
    sql='select count(*) from jobdata'
    cursor.execute(sql)    #执行sql语句  
    results = cursor.fetchall()
    for (i,) in results:
        result = i
    cursor.close()
    db.close()
    return result

def getFailCount():
    db = pymysql.connect(**sqlsetting.con())
    cursor = db.cursor()
    sql='select count(*) from jobdata where avgSalary=0 or (grade="中级" and  avgSalary>45) or (grade="高级" and  avgSalary>70) or industry="" or financeStage="" or companySize=""'
    cursor.execute(sql)    #执行sql语句  
    results = cursor.fetchall()
    for (i,) in results:
        result = i
    cursor.close()
    db.close()
    return result


def getCount(request):
    body={}
    try:
        body['interNum']=1
        body['count']=getSucCount()
        body['failCount']=getFailCount()
        body['vaildCount']=body['count']-body['failCount']
        result=resp.handle(body,True)
    except:
        body='Error'
        result=resp.handle(body,False)
    return JsonResponse(result, safe=False)


def getPJob(request):
    body = {}
    db = pymysql.connect(**sqlsetting.con())
    cursor = db.cursor()
    sql='select secondType, count(*) AS count from jobdata group by positionName order by count desc'
    try:
        cursor.execute(sql)    #执行sql语句  
        results = cursor.fetchall()
        xAxis=[]
        series=[]
        for row in results:
            if(row[1]>450):
                positionName=row[0]
                hotdata=row[1]
                xAxis.append(positionName)
                series.append(hotdata)
        body['series'] = series
        body['gradeName'] = xAxis
        result=resp.handle(body,True)
    except:
        body = 'Error'
        result=resp.handle(body,False)
    return JsonResponse(result, safe=False)

    
def getPCom(request):
    body = {}
    db = pymysql.connect(**sqlsetting.con())
    cursor = db.cursor()
    sql='select companyFullName, count(*) AS count from jobdata group by companyFullName order by count desc'
    try:
        cursor.execute(sql)    #执行sql语句  
        results = cursor.fetchall()
        xAxis=[]
        series=[]
        for row in results:
            if(row[1]>200):
                positionName=row[0]
                hotdata=row[1]
                xAxis.append(positionName)
                series.append(hotdata)
        body['series'] = series
        body['gradeName'] = xAxis
        result=resp.handle(body,True)
    except:
        body = 'Error'
        result=resp.handle(body,False)
    return JsonResponse(result, safe=False)

def getPCity(request):
    body={}
    db = pymysql.connect(**sqlsetting.con())
    cursor = db.cursor()
    sql='select city, count(*) AS count from jobdata group by city order by count desc'
    try:
        cursor.execute(sql)    #执行sql语句  
        results = cursor.fetchall()
        xAxis=[]
        series=[]
        for row in results:
            if(row[1]>500):
                positionName=row[0]
                hotdata=row[1]
                xAxis.append(positionName)
                series.append(hotdata)
        body['series'] = series
        body['gradeName'] = xAxis
        result=resp.handle(body,True)
    except:
        body = 'Error'
        result=resp.handle(body,False)
    return JsonResponse(result, safe=False)


def getCList(request):
    body={}
    db = pymysql.connect(**sqlsetting.con())
    cursor = db.cursor()
    sql='select name from bosscity'
    citylist = []
    try:
        cursor.execute(sql)    #执行sql语句  
        results = cursor.fetchall()
        for (row,) in results:
            citylist.append(row)
        body['citylist'] = citylist
        result=resp.handle(body,True)
    except:
        body = 'Error'
        result=resp.handle(body,False)
    return JsonResponse(result, safe=False)


def getIList(request):
    body={}
    db = pymysql.connect(**sqlsetting.con())
    cursor = db.cursor()
    sql='select name from industry'
    industryList = []
    try:
        cursor.execute(sql)    #执行sql语句  
        results = cursor.fetchall()
        for (row,) in results:
            industryList.append(row)
        body['industryList'] = industryList
        result=resp.handle(body,True)
    except:
        body = 'Error'
        result=resp.handle(body,False)
    return JsonResponse(result, safe=False)


