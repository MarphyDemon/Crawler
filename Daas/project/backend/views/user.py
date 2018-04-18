from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from django.db.models.functions import TruncDate
import pymysql
from backend.views import resp
import time
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

#注册
def regist(request):
    body={}
    db = pymysql.connect(**config)
    cursor = db.cursor()
    username = request.POST.get('username',None)
    phoneNum = request.POST.get('phoneNum',None)
    email = request.POST.get('email',None)
    password = request.POST.get('password',None) 
    date_joined = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sqlC = 'select username from auth_user where username=%s or email=%s or phoneNum=%s'
    res = cursor.execute(sqlC,(username,email,phoneNum))
    if res:
        body['msg'] = '已有账号，请登录！'
        result=resp.handle(body,True)
    else:
        sql = "insert into auth_user(username,phoneNum,email,password,date_joined,is_superuser)values (%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(sql,(username,phoneNum,email,password,date_joined,'0'))
            db.commit()
            body['msg'] = '1'
            result=resp.handle(body,True)
        except:
            body = 'Error'
            result=resp.handle(body,False)
    cursor.close()
    db.close()
    return JsonResponse(result, safe=False)
        

#登陆
def login(request):
    body={}
    db = pymysql.connect(**config)
    cursor = db.cursor()
    username = request.POST.get('username',None)
    password = request.POST.get('password',None) 
    sql = "select username from auth_user where (username=%s or email=%s or phoneNum=%s) and password=%s"
    try:
        res = cursor.execute(sql,(username,username,username,password))
        results = cursor.fetchall()
        if res:
            for (row,) in results:
                result = row
            body['msg'] = '1'
            body['username']=result
            result=resp.handle(body,True)
        else:
            body['msg'] = '输入用户名或密码错误'
            result=resp.handle(body,True)
    except:
        body = 'Error'
        result=resp.handle(body,False)
    cursor.close()
    db.close()
    return JsonResponse(result, safe=False)

#登陆成功
def index(request):
    body={}
    username = request.COOKIES.get('username','')
    body['msg'] = '1'
    result=resp.handle(body,True)
    return JsonResponse(result, safe=False)

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    body['msg'] = '退出'
    result=resp.handle(body,True)
    return JsonResponse(result, safe=False)