#_*_  coding: utf-8 _*_
# Author: waltsmith
# Date:2018-01-03
# 导入模块
import pymysql

## 建立腾讯jobs数据库
# 创建连接
Connection = pymysql.connect(database='tencent', host='localhost', user='root', password='marphy0817')

cursor = Connection.cursor()
# 创建jobs表
sql_create_table = '''
    create table jobs(job_name varchar (100),
      location varchar (40),
      type varchar (40),
      needed_people_num varchar (5),
      duty varchar (400),
      requirement varchar (500)
    )
'''
# 执行sql语句，创建jobs表
cursor.execute(sql_create_table)
# 提交
Connection.commit()
# 断开连接
Connection.close()
print("数据库创建完毕！！")



