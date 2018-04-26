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


def getfirstDate(grade,positionName,year,month):
    db = pymysql.connect(**sqlsetting.con())
    cursor = db.cursor()
    positionName = '%'+positionName+'%'
    # year = year + '-%'
    # month = '%-'+month+"-%"
    datestr = year + '-%'+month+"-%"
    if year and month:
        sql='select count(*) from jobdata where grade= %s and positionName like %s and createTime like %s and avgSalary>0 and industry!=""'
        cursor.execute(sql,(grade,positionName,datestr))    #执行sql语句  
    else:
        sql='select count(*) from jobdata where grade= %s and positionName like %s and avgSalary>0 and industry!=""'
        cursor.execute(sql,(grade,positionName))
    results = cursor.fetchall()
    result= 0
    if results:
        for (i,) in results:
            result = i
    else:
       result = 0
    cursor.close()
    db.close()
    return result

def getMonth(request):
    seriesList = []
    seriesChild = {}
    seriesData = []
    body = {}
    positionName = request.POST.get('positionName',None)
    year = request.POST.get('year',None)
    try:
        gradeArray = ['入门','初级','中级','高级','专家','不限']
        gradeName = ['01','02','03','04','05','06','07','08','09','10','11','12']
        for i in gradeArray:
            seriesData=[]
            seriesChild={}
            for j in gradeName:
                count = getfirstDate(i,positionName,year,j)
                seriesData.append(count)
            seriesChild['name']=i
            seriesChild['data']=seriesData
            seriesList.append(seriesChild)
        body['series'] = seriesList
        body['gradeName'] = gradeName
        result=resp.handle(body,True)
    except:
        body = 'Error'
        result=resp.handle(body,False)
    return JsonResponse(result, safe=False)

