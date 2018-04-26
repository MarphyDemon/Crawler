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

def getfirstStage(grade,positionName,city,Stage):
    global MinSalarylist
    global MaxSalarylist
    global AvgSalarylist
    db = pymysql.connect(**sqlsetting.con())
    cursor = db.cursor()
    positionName = '%'+positionName+'%'
    if city and Stage:
        sql='select avgSalary from jobdata where grade= %s and positionName like %s and city= %s and financeStage= %s and avgSalary>0 and industry!="" order by avgSalary'
        cursor.execute(sql,(grade,positionName,city,Stage))    #执行sql语句  
    elif city and Stage=='':
        sql='select avgSalary from jobdata where grade= %s and positionName like %s and city= %s and avgSalary>0 and industry!="" order by avgSalary'
        cursor.execute(sql,(grade,positionName,city))
    elif city=='' and Stage:
        sql='select avgSalary from jobdata where grade= %s and positionName like %s and financeStage= %s and avgSalary>0 and industry!="" order by avgSalary'
        cursor.execute(sql,(grade,positionName,Stage))
    else:
        sql='select avgSalary from jobdata where grade= %s and positionName like %s and avgSalary>0 and industry!="" order by avgSalary'
        cursor.execute(sql,(grade,positionName))
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

def getStage(request):
    global MinSalarylist
    global MaxSalarylist
    global AvgSalarylist
    SalaryList = [{},{},{}]
    MinSalarylist = []
    MaxSalarylist = []
    AvgSalarylist = []
    body = {}
    positionName = request.POST.get('positionName',None) 
    city = request.POST.get('city',None) 
    Stage = request.POST.get('Stage',None)
    try:
        getfirstStage('入门',positionName,city,Stage)
        getfirstStage('初级',positionName,city,Stage)
        getfirstStage('中级',positionName,city,Stage)
        getfirstStage('高级',positionName,city,Stage)
        getfirstStage('专家',positionName,city,Stage)
        getfirstStage('不限',positionName,city,Stage)
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

