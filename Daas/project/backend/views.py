from django.shortcuts import render
from django.http import JsonResponse
from django.db.models.functions import TruncDate
import pymysql
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


def getData(request):
    print(request)
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql='select count(*) from lagou'
    cursor.execute(sql)    #执行sql语句  
    results = cursor.fetchall()
    print(results)
    return JsonResponse(results, safe=False)
