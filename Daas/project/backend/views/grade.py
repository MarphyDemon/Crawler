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

SalaryList = [{},{},{}]
MinSalarylist = []
MaxSalarylist = []
AvgSalarylist = []

def getfirstGrade(grade,positionName):
    global MinSalarylist
    global MaxSalarylist
    global AvgSalarylist
    db = pymysql.connect(**sqlsetting.con())
    cursor = db.cursor()
    positionName = '%'+positionName+'%'
    sql='select avgSalary from jobdata where grade= %s and positionName like %s and avgSalary>0 and industry!="" order by avgSalary'
    cursor.execute(sql,(grade,positionName))    #执行sql语句  
    results = cursor.fetchall()
    result=[]
    Sum = 0
    if results:
        for (i,) in results:
            result.append(i*1000)
            Sum=Sum+int(i*1000)
        avgS = float('%.2f' % (Sum/len(result)))
        minS = result[0]
        length = len(result)-1
        maxS = result[length]
        if(maxS>(avgS*2)):
            maxS = avgS + 5520
    else:
        minS=''
        maxS=''
        avgS=''

    MinSalarylist.append(minS)
    MaxSalarylist.append(maxS)
    AvgSalarylist.append(avgS)
    cursor.close()
    db.close()

def getGrade(request):
    global MinSalarylist
    global MaxSalarylist
    global AvgSalarylist
    SalaryList = [{},{},{}]
    MinSalarylist = []
    MaxSalarylist = []
    AvgSalarylist = []
    body = {}
    positionName = request.POST.get('positionName',None) 
    try:
        getfirstGrade('入门',positionName)
        getfirstGrade('初级',positionName)
        getfirstGrade('中级',positionName)
        getfirstGrade('高级',positionName)
        getfirstGrade('专家',positionName)
        getfirstGrade('不限',positionName)
        SalaryList[0]['name'] = '最低工资'
        SalaryList[0]['data'] = MinSalarylist
        SalaryList[1]['name'] = '平均工资'
        SalaryList[1]['data'] = AvgSalarylist
        SalaryList[2]['name'] = '最高工资'
        SalaryList[2]['data'] = MaxSalarylist
        gradeName = ['入门','初级','中级','高级','专家','不限']
        body['gradeName'] = gradeName
        body['series'] = SalaryList
        result=resp.handle(body,True)
    except:
        body = 'Error'
        result=resp.handle(body,False)
    return JsonResponse(result, safe=False)


def getGradeSalary(grade,positionName):
    db = pymysql.connect(**sqlsetting.con())
    cursor = db.cursor()
    positionName = '%'+positionName+'%'
    sql='select avgSalary from jobdata where grade= %s and positionName like %s and avgSalary>0 order by avgSalary'
    cursor.execute(sql,(grade,positionName))    #执行sql语句  
    results = cursor.fetchall()
    result=[]
    Sum = 0
    for (i,) in results:
        result.append(i)
    cursor.close()
    db.close()
    return result


def getSGrade(request):
    SalaryList = [{},{},{},{},{}]
    body = {}
    positionName = request.POST.get('positionName',None) 
    try:
        first = getGradeSalary('入门',positionName)
        second = getGradeSalary('初级',positionName)
        three = getGradeSalary('中级',positionName)
        four = getGradeSalary('高级',positionName)
        five = getGradeSalary('专家',positionName)
        SalaryList[0]['name'] = '入门'
        SalaryList[0]['data'] = first
        SalaryList[1]['name'] = '初级'
        SalaryList[1]['data'] = second
        SalaryList[2]['name'] = '中级'
        SalaryList[2]['data'] = three
        SalaryList[3]['name'] = '高级'
        SalaryList[3]['data'] = four
        SalaryList[4]['name'] = '专家'
        SalaryList[4]['data'] = five
        gradeName = ['入门','初级','中级','高级','专家']
        body['gradeName'] = gradeName
        body['series'] = SalaryList
        result=resp.handle(body,True)
    except:
        body = 'Error'
        result=resp.handle(body,False)
    return JsonResponse(result, safe=False)