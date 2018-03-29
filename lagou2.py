#create by 矜持的折返跑
import time
import requests
import pymysql
import json

config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"marphy0817",
    "database":"lagouone",
    "charset":"utf8"
}
# results=[]
# def getCity():
    # db = pymysql.connect(**config)
    # cursor = db.cursor()
    # sql = "select city from citylist"  
    # try:  
    #     cursor.execute(sql)    #执行sql语句  
    #     results = cursor.fetchall()
    # except:
    #     print("Error")
    #     pass
def lagou(page,city):
    # if (page==146) and city== '北京':
    #     lagou(page+1,city)
    #     db = pymysql.connect(**config)
    #     db.close()
            
    print('---------------------第',city,page,'页--------------------')
    headers = {'Referer':'https://www.lagou.com/jobs/list_?labelWords=&fromSearch=true&suginput=',               'Origin':'https://www.lagou.com',                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
               'Accept':'application/json, text/javascript, */*; q=0.01',
               'Cookie':'JSESSIONID=ABAAABAAAGFABEFE8A2337F3BAF09DBCC0A8594ED74C6C0; user_trace_token=20180122215242-849e2a04-ff7b-11e7-a5c6-5254005c3644; LGUID=20180122215242-849e3549-ff7b-11e7-a5c6-5254005c3644;  _gat=1; TG-TRACK-CODE=index_navigation; _gid=GA1.2.1188502030.1516629163; _ga=GA1.2.667506246.1516629163; LGSID=20180122215242-849e3278-ff7b-11e7-a5c6-5254005c3644; LGRID=20180122230310-5c6292b3-ff85-11e7-a5d5-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516629163,1516629182; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516633389; SEARCH_ID=8d3793ec834f4b0e8e680572b83eb968'
               }
    dates={'first':'true',
           'pn': page,
           'kd': ''}
    url='https://www.lagou.com/jobs/positionAjax.json?px=new&city='+city+'&needAddtionalResult=false'
    # url='https://www.lagou.com/jobs/positionAjax.json?city='+city+'&needAddtionalResult=false&isSchoolJob=0'
    # print(url)
    resp = requests.post(url,data=dates,headers=headers)
    print(resp.content.decode('utf-8'))
    result=resp.json()['content']['positionResult']['result']
    resultSize=int(resp.json()['content']['positionResult']['totalCount']/15)+1
    if page <= resultSize and result!=[]:
        db = pymysql.connect(**config)
        positionName = []
        for i in result:
            cursor = db.cursor()
            count=0

            positionName.append(i['positionName'])
            timeNow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            #连接数据库
            if i['businessZones']:
                businessZones = "".join(i['businessZones'])
            else:
                businessZones=""

            if i['companyLabelList']:
                companyLabelList = "".join(i['companyLabelList'])
            else:
                companyLabelList=""

            if i['industryLables']:
                industryLables = "".join(i['industryLables'])
            else:
                industryLables=""

            if i['positionLables']:
                positionLables = "".join(i['positionLables'])
            else:
                positionLables=""
            sqlExit = "select positionIdInLagou from lagou where positionIdInLagou = '%s'" % (i['positionId'])
            res = cursor.execute(sqlExit)
            if res:
                print('数据已存在', res)
                cursor.close()
            else:
                print("aa")
                sql = "insert into lagou(positionName,workYear,salary,companyShortName\
                    ,companyIdInLagou,education,jobNature,positionIdInLagou,createTimeInLagou\
                    ,city,industryField,positionAdvantage,companySize,score,positionLables\
                    ,industryLables,publisherId,financeStage,companyLabelList,district,businessZones\
                    ,companyFullName,firstType,secondType,isSchoolJob,subwayline\
                    ,stationname,linestaion,resumeProcessRate,createByMe,keyByMe\
                )VALUES (%s,%s,%s,%s, \
                    %s,%s,%s,%s,%s\
                    ,%s,%s,%s,%s,%s,%s,%s\
                    ,%s,%s,%s,%s,%s\
                    ,%s,%s,%s,%s,%s\
                    ,%s,%s,%s,%s,%s\
                    )"
                try:
                    print("1122")
                    print(i)
                    print(positionLables,companyLabelList,businessZones,timeNow,industryLables)
                    print(i['positionName'],i['workYear'],i['salary'],i['companyShortName']
                                    ,i['companyId'],i['education'],i['jobNature'],i['positionId'],i['createTime']
                                    ,i['city'],i['industryField'],i['positionAdvantage'],i['companySize'],i['score'],positionLables
                                    ,industryLables,i['publisherId'],i['financeStage'],companyLabelList,i['district'],businessZones
                                    ,i['companyFullName'],i['firstType'],i['secondType'],i['isSchoolJob'],i['subwayline']
                                    ,i['stationname'],i['linestaion'],i['resumeProcessRate'],timeNow,i['positionName']
                                    ,'lidong')
                    cursor.execute(sql,(i['positionName'],i['workYear'],i['salary'],i['companyShortName']
                                    ,i['companyId'],i['education'],i['jobNature'],i['positionId'],i['createTime']
                                    ,i['city'],i['industryField'],i['positionAdvantage'],i['companySize'],i['score'],positionLables
                                    ,industryLables,i['publisherId'],i['financeStage'],companyLabelList,i['district'],businessZones
                                    ,i['companyFullName'],i['firstType'],i['secondType'],i['isSchoolJob'],i['subwayline']
                                    ,i['stationname'],i['linestaion'],i['resumeProcessRate'],timeNow,i['positionName']
                                    ))
                    db.commit()  #提交数据
                    cursor.close()
                    count=count+1
                except:
                    conn.rollback()
        page=page+1
        db.close()  
        lagou(page,city)
        time.sleep(1)
    else:
        print(city+'已保存完')
        
def main():
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "select name from bosscity"  
    try:  
        cursor.execute(sql)    #执行sql语句  
        results = cursor.fetchall()
        for (i,) in results:
            print('开始',i,'城市的数据爬取')
            lagou(1,i)
    except:
        print("Error")
        pass
    cursor.close()
    db.close()
#输入你想要爬取的职位名,如:python
if __name__ == '__main__':
    main()



# bug1 爬取北京在146页卡掉