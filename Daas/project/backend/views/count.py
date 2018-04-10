from django.shortcuts import render
from django.http import JsonResponse
from django.db.models.functions import TruncDate
import pymysql
from backend.views import resp
# Create your views here.
import logging
# Get an instance of a logger
logger = logging.getLogger('sourceDns.webdns.views')
config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"marphy0817",
    "database":"lagouone",
    "charset":"utf8"
}
def getCount(request):
    body={}
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql='select * from jobcount'
    try:
        cursor.execute(sql)    #执行sql语句  
        results = cursor.fetchall()
        countArr=[]
        for i in results:
            for j in i:
                countArr.append(j)
        body['count']=countArr[1]
        body['failCount']=countArr[2]
        result=resp.handle(body,True)
    except:
        body='Error'
        result=resp.handle(body,False)
    cursor.close()
    db.close()
    return JsonResponse(result, safe=False)
