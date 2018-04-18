#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 多进程爬取拉勾网招聘数据   

#动态添加User-Agent  添加反扒技术

import time
from multiprocessing import Pool
from datetime import timedelta
from tornado import httpclient, gen, ioloop, queues
import time
import requests
import pymysql
import json
import clearMethod
import random

config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"marphy0817",
    "database":"lagouone",
    "charset":"utf8"
}

UA_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
proxies = {
    'http': 'http://123.206.6.17:3128',
    'https': 'http://123.206.6.17:3128'
}
page = 1
class AsySpider(object):
    """A simple class of asynchronous spider."""
    def __init__(self, urls, concurrency):
        urls.reverse()
        self.urls = urls
        self.concurrency = concurrency
        self._q = queues.Queue()
        self._fetching = set()
        self._fetched = set()
        
    def handle_page(self, url, html):
        global page
        # print(page)
        # print('---------------------第',page,'页--------------------')
        headers = {'Referer':'https://www.lagou.com/jobs/list_?px=new&city=%E5%85%A8%E5%9B%BD',
                    'Origin':'https://www.lagou.com',                
                    'User-Agent': random.choice(UA_LIST),
                    'Accept':'application/json, text/javascript, */*; q=0.01',
                    'Cookie':'_ga=GA1.2.1709143610.1517467315; user_trace_token=20180201144155-fe5ee656-071a-11e8-abe5-5254005c3644; LGUID=20180201144155-fe5ee97c-071a-11e8-abe5-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAACEBACDGD36A22529D191C696E92A320C0B3BF7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1520823130,1523069798; TG-TRACK-CODE=index_search; _gat=1; LGSID=20180409170942-bd55942c-3bd5-11e8-b741-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%3Fpx%3Dnew%26hy%3D%25E7%25A7%25BB%25E5%258A%25A8%25E4%25BA%2592%25E8%2581%2594%25E7%25BD%2591%26city%3D%25E5%258C%2597%25E4%25BA%25AC; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1523265009; LGRID=20180409171007-cc6f875d-3bd5-11e8-b741-5254005c3644; SEARCH_ID=d8b6c61ef7214f7786c365fee2bdf950'
                    }
        dates={'first': 'true',
            'pn': page,
            'kd': ''}
        
        # url='https://www.lagou.com/jobs/positionAjax.json?px=new&city='+city+'&needAddtionalResult=false'
        # url='https://www.lagou.com/jobs/positionAjax.json?city='+city+'&needAddtionalResult=false&isSchoolJob=0'
        # print(url,'lidongdongdongdong')
        print('---url为----'+str(url)+'----页码---'+str(page)+'-----')
        resp = requests.post(url,data=dates,headers=headers)
        # print(resp)
        print(resp.content.decode('utf-8'))
        result=resp.json()['content']['positionResult']['result']
        # resultSize=int(resp.json()['content']['positionResult']['totalCount']/15)+1
        print(str(url)+'总数为：-----'+str(resp.json()['content']['positionResult']['totalCount']))
        if result!=[]:
            db = pymysql.connect(**config)
            positionName = []
            for i in result:
                cursor = db.cursor()
                positionName.append(i['positionName'])
                timeNow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                sqlExit = "select positionId from jobdata where positionId = '%s'" % (i['positionId'])
                res = cursor.execute(sqlExit)
                # print('res','lidong')
                grade = clearMethod.getJobGrade(i['workYear'])
                avgSalary = clearMethod.getJobSalary(i['salary'])
                industry = clearMethod.getIndustry(i['industryField'])
                # date = clearMethod.getMonth(i['createTime'])
                # print('industry',industry)
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

                        # ,year,month\
                        # ,%s,%s\
                    try:
                        cursor.execute(sql,(i['positionName'],i['workYear'],i['salary']
                                        ,i['education'],i['jobNature'],i['positionId'],i['createTime']
                                        ,i['city'],i['industryField'],i['companySize']
                                        ,i['financeStage'],i['secondType'],timeNow
                                        ,grade,avgSalary,industry,i['companyFullName']
                                        # ,date['year'],date['month']
                                        ))
                        db.commit()  #提交数据
                        cursor.close()
                    except:
                        db.rollback()
            page=page+1
            db.close()  
            self.handle_page(url, html)
            time.sleep(2)
        else:
            print('已保存完')

    @gen.coroutine
    def get_page(self, url):
        try:
            response = yield httpclient.AsyncHTTPClient().fetch(url)
            print('######fetched %s' % url)
        except Exception as e:
            print('Exception: %s %s' % (e, url))
            raise gen.Return('')
        raise gen.Return(response.body)

    @gen.coroutine
    def _run(self):

        @gen.coroutine
        def fetch_url():
            current_url = yield self._q.get()
            try:
                if current_url in self._fetching:
                    return
                print('fetching****** %s' % current_url)
                self._fetching.add(current_url)
                html = yield self.get_page(current_url)
                self._fetched.add(current_url)
    
                self.handle_page(current_url, html)
    
                for i in range(self.concurrency):
                    if self.urls:
                        yield self._q.put(self.urls.pop())

            finally:
                self._q.task_done()

        @gen.coroutine
        def worker():
            while True:
                yield fetch_url()

        self._q.put(self.urls.pop())

        # Start workers, then wait for the work queue to be empty.
        for _ in range(self.concurrency):
            worker()
        yield self._q.join(timeout=timedelta(seconds=30000))
        assert self._fetching == self._fetched

    def run(self):
        io_loop = ioloop.IOLoop.current()
        io_loop.run_sync(self._run)

def run_spider(city):
    urls = []
    urls.append('https://www.lagou.com/jobs/positionAjax.json?px=new&city='+city+'&needAddtionalResult=false')
    print('---------------开始'+city+'爬取---------------')
    s = AsySpider(urls, 16)
    s.run()

def main():
    _st = time.time()
    p = Pool()
    # all_num = 73000
    # num = 4 # number of cpu cores
    # per_num, left = divmod(all_num, num)
    # s = range(0, all_num, per_num)
    res = []
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "select name from bosscity"  
    try: 
        cursor.execute(sql)    #执行sql语句  
        results = cursor.fetchall()
        for (i,) in results:
            res.append(i)
        # print(res)
        for i in res:
            p.apply_async(run_spider, args=(i,))
        p.close()
        p.join()
        print(time.time()-_st)
    except:
        print("Error")
        pass
    cursor.close()
    db.close()

if __name__ == '__main__':
    main()