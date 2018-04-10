#create by lidongdong

#第一次尝试数据清洗
import time
import requests
import pymysql
import json
import clearMethod

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
    headers = {'Referer':'https://www.lagou.com/jobs/list_?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',               'Origin':'https://www.lagou.com',                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
               'Accept':'application/json, text/javascript, */*; q=0.01',
               'Cookie':'_ga=GA1.2.1709143610.1517467315; user_trace_token=20180201144155-fe5ee656-071a-11e8-abe5-5254005c3644; LGUID=20180201144155-fe5ee97c-071a-11e8-abe5-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAACEBACDGD36A22529D191C696E92A320C0B3BF7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1520823130,1523069798; TG-TRACK-CODE=index_search; _gat=1; LGSID=20180409170942-bd55942c-3bd5-11e8-b741-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%3Fpx%3Dnew%26hy%3D%25E7%25A7%25BB%25E5%258A%25A8%25E4%25BA%2592%25E8%2581%2594%25E7%25BD%2591%26city%3D%25E5%258C%2597%25E4%25BA%25AC; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1523265009; LGRID=20180409171007-cc6f875d-3bd5-11e8-b741-5254005c3644; SEARCH_ID=d8b6c61ef7214f7786c365fee2bdf950'
               }
    dates={'first':'true',
           'pn': page,
           'kd': ''}
    url='https://www.lagou.com/jobs/positionAjax.json?px=new&city='+city+'&needAddtionalResult=false'
    # url='https://www.lagou.com/jobs/positionAjax.json?city='+city+'&needAddtionalResult=false&isSchoolJob=0'
    # print(url)
    resp = requests.post(url,data=dates,headers=headers)
    print(resp)
    print(resp.content.decode('utf-8'))
    result=resp.json()['content']['positionResult']['result']
    resultSize=int(resp.json()['content']['positionResult']['totalCount']/15)+1
    if page <= resultSize and result!=[]:
        db = pymysql.connect(**config)
        positionName = []
        for i in result:
            cursor = db.cursor()
            positionName.append(i['positionName'])
            timeNow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            sqlExit = "select positionId from jobdata where positionId = '%s'" % (i['positionId'])
            res = cursor.execute(sqlExit)
            print('res','lidong')
            grade = clearMethod.getJobGrade(i['workYear'])
            avgSalary = clearMethod.getJobSalary(i['salary'])
            industry = clearMethod.getIndustry(i['industryField'])
            print('industry',industry)
            # if(industry == 'false'):
            #     page=page+1
            #     lagou(page,city)
            # companyValue = clearMethod.getCompanyValue(i['financeStage'])
            # else:
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
                try:
                    cursor.execute(sql,(i['positionName'],i['workYear'],i['salary']
                                    ,i['education'],i['jobNature'],i['positionId'],i['createTime']
                                    ,i['city'],i['industryField'],i['companySize']
                                    ,i['financeStage'],i['secondType'],timeNow
                                    ,grade,avgSalary,industry,i['companyFullName']
                                    ))
                    db.commit()  #提交数据
                    cursor.close()
                except:
                    conn.rollback()
        page=page+1
        db.close()  
        lagou(page,city)
        time.sleep(2)
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