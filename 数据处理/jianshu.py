#create by lidongdong
import time
import requests
import pymysql
import json

# config={
#     "host":"127.0.0.1",
#     "user":"root",
#     "password":"marphy0817",
#     "database":"lagouone",
#     "charset":"utf8"
# }
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
def jianshu():
    headers = {'Referer':'https://www.jianshu.com/search?q=%E5%B0%8F%E7%A8%8B%E5%BA%8F&page=1&type=note',               'Origin':'https://www.jianshu.com',                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
               'Accept':'application/json, gzip, deflate, br, zh-CN,zh;q=0.9',
               'Cookie':'read_mode=day; default_font=font2; locale=zh-CN; _m7e_session=a6a215704a0d038733652a976ef512dc; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1533799464,1535706151,1535958599; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1535958599; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221653b72051978d-081b9b4620e30b-34677908-1764000-1653b72051a129%22%2C%22%24device_id%22%3A%221653b72051978d-081b9b4620e30b-34677908-1764000-1653b72051a129%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com.hk%2F%22%2C%22%24latest_referrer_host%22%3A%22www.google.com.hk%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22search-trending%22%7D%7D; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fsearch%3Fq%3D%25E5%25B0%258F%25E7%25A8%258B%25E5%25BA%258F%26page%3D1%26type%3Dnote'
               }
    dates={ 'q': '小程序',
            'type': 'note',
            'page': '1',
            'order_by': 'default'}
    url='https://www.jianshu.com/search/do?q=%E5%B0%8F%E7%A8%8B%E5%BA%8F&type=note&page=1&order_by=default'
    # url='https://www.lagou.com/jobs/positionAjax.json?city='+city+'&needAddtionalResult=false&isSchoolJob=0'
    # print(url)
    resp = requests.post(url,data=dates,headers=headers)
    print(resp.content.decode('utf-8'))
    # result=resp.json()['content']['positionResult']['result']
    # resultSize=resp.json()['content']['positionResult']['resultSize']
    # print(resultSize)
    # db = pymysql.connect(**config)
    # positionName = []
    # for i in result:
    #     print(i)
    #     count=0
    #     positionName.append(i['positionName'])
    #     timeNow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     #连接数据库
    #     cursor = db.cursor()
    #     if i['businessZones']:
    #         businessZones = "".join(i['businessZones'])
    #     else:
    #         businessZones=""

    #     if i['companyLabelList']:
    #         companyLabelList = "".join(i['companyLabelList'])
    #     else:
    #         companyLabelList=""

    #     if i['industryLables']:
    #         industryLables = "".join(i['industryLables'])
    #     else:
    #         industryLables=""

    #     if i['positionLables']:
    #         positionLables = "".join(i['positionLables'])
    #     else:
    #         positionLables=""
    #     print(i['positionId'],"hfaksdjhsalidongdong")
    #     sqlExit = "select positionIdInLagou from lagou where positionIdInLagou = '%s'" % (i['positionId'])
    #     res = cursor.execute(sqlExit)
    #     if res:
    #         print('数据已存在', res)
    #         cursor.close()
    #     else:
    #         sql = "insert into lagou(positionName,workYear,salary,companyShortName\
    #             ,companyIdInLagou,education,jobNature,positionIdInLagou,createTimeInLagou\
    #             ,city,industryField,positionAdvantage,companySize,score,positionLables\
    #             ,industryLables,publisherId,financeStage,companyLabelList,district,businessZones\
    #             ,companyFullName,firstType,secondType,isSchoolJob,subwayline\
    #             ,stationname,linestaion,resumeProcessRate,createByMe,keyByMe\
    #         )VALUES (%s,%s,%s,%s, \
    #             %s,%s,%s,%s,%s\
    #             ,%s,%s,%s,%s,%s,%s,%s\
    #             ,%s,%s,%s,%s,%s\
    #             ,%s,%s,%s,%s,%s\
    #             ,%s,%s,%s,%s,%s\
    #             )"

    #         cursor.execute(sql,(i['positionName'],i['workYear'],i['salary'],i['companyShortName']
    #                             ,i['companyId'],i['education'],i['jobNature'],i['positionId'],i['createTime']
    #                             ,i['city'],i['industryField'],i['positionAdvantage'],i['companySize'],i['score'],positionLables
    #                             ,industryLables,i['publisherId'],i['financeStage'],companyLabelList,i['district'],businessZones
    #                             ,i['companyFullName'],i['firstType'],i['secondType'],i['isSchoolJob'],i['subwayline']
    #                             ,i['stationname'],i['linestaion'],i['resumeProcessRate'],timeNow,position
    #                             ))
    #         db.commit()  #提交数据
    #         cursor.close()
    #         count=count+1
    # db.close()
    # time.sleep(1)
            
# def main():
#     db = pymysql.connect(**config)
#     cursor = db.cursor()
#     sql = "select * from citylist order by letter ASC"  
#     try:  
#         cursor.execute(sql)    #执行sql语句  
#         results = cursor.fetchall()
#         for i in results:
#             city = str(i)
#             page = 1
#             while page<=30:
#                 print('---------------------第',city[2:4],page,'页--------------------')
#                 lagou(page,position,city[2:4])
#                 # lagou(page,position,'%E9%9E%8D%E5%B1%B1')
#                 page=page+1
#     except:
#         print("Error")
#         pass
if __name__ == '__main__':
    jianshu()