#create by lidongdong
#  用于清洗第一次爬取的拉勾数据



import time
import requests
import pymysql
import json
import clearMethod
import pandas as pd

config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"marphy0817",
    "database":"lagouone",
    "charset":"utf8"
}

def getOldData(row):
    print(row)
    db = pymysql.connect(**config)
    cursor = db.cursor()
    positionName = row[0]
    workYear = row[1]
    salary = row[2]
    education = row[5]
    jobNature = row[6]
    positionId = row[7]
    createTime = row[8]
    print('0')
    city = row[9]
    industryField = row[10]           
    companySize = row[27]
    financeStage = row[13]
    secondType = row[19]
    print('1')
    timeNow = row[26]
    grade = clearMethod.getJobGrade(workYear)
    avgSalary = clearMethod.getJobSalary(salary)
    print('2')
    industry = clearMethod.getIndustry(industryField)
    # date = clearMethod.getMonth(createTime)
    companyFullName = row[17]
    print('3')
    sqlExit = "select positionId from jobdata where positionId = '%s'" % (positionId)
    print('545')
    res = cursor.execute(sqlExit)
    print('2323')
    print(res,'res')
    print(positionName,workYear,salary
                            ,education,jobNature,positionId,createTime
                            ,city,industryField,companySize
                            ,financeStage,secondType,timeNow
                            ,grade,avgSalary,industry,companyFullName
                            )
    if res:
        print('数据已存在', res)
        cursor.close()
    else:

        sql = "insert into jobdata(positionName,workYear,salary\
            ,education,jobNature,positionId,createTime\
            ,city,industryField,companySize\
            ,financeStage,secondType,createByMe\
            ,grade,avgSalary,industry,companyFullName\
        )VALUES (%s,%s,%s\
            ,%s,%s,%s,%s\
            ,%s,%s,%s\
            ,%s,%s,%s\
            ,%s,%s,%s,%s\
            )"
            # ,year,month\
            # ,%s,%s\
        try:
            print('233','dsdhjs')
            cursor.execute(sql,(positionName,workYear,salary
                            ,education,jobNature,positionId,createTime
                            ,city,industryField,companySize
                            ,financeStage,secondType,timeNow
                            ,grade,avgSalary,industry,companyFullName
                            # ,date['year'],date['month']
                            ))
        except:
            conn.rollback()
        db.commit()  #提交数据
        cursor.close()
    db.close()

def main():
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "select * from lagou"  
    try:  
        cursor.execute(sql)    #执行sql语句  
        results = cursor.fetchall()
        for row in results:
            getOldData(row)
    except:
        print('Error')
    cursor.close()
    db.close()

if __name__ == '__main__':
    main()



# bug1 爬取北京在146页卡掉