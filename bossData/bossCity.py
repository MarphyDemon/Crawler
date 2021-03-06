#create by lidongdong
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
def crawlcity():
    headers = {'Referer':'https://www.zhipin.com/common/data/city.json',               'Origin':'https://www.zhipin.com',                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
               'Accept':'application/json, text/javascript, */*; q=0.01',
               'Cookie':'JSESSIONID=""; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1520823369,1520823381,1522231558; __c=1522231566; __l=r=https%3A%2F%2Fwww.zhipin.com%2F&l=%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3D%26scity%3D101010100%26industry%3D%26position%3D; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fjob_detail%2F1418574492.html%3Fka%3Dsearch_list_1; lastCity=101020100; __a=52508175.1522231554.1522231554.1522231566.48.2.47.48; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1522242845'
               }
    url='https://www.zhipin.com/common/data/city.json'
    resp = requests.post(url,headers=headers)
    results = resp.json()['data']['cityList']
    db = pymysql.connect(**config)
    for i in results:
        if(i['subLevelModelList']):
            for a in i['subLevelModelList']:
                cursor = db.cursor()
                sqlExit = "select code from bosscity where code = '%s'" % (a['code'])
                res = cursor.execute(sqlExit)
                if res:
                    print('数据已存在', res)
                    cursor.close()
                else:
                    sql = "insert into bosscity(code,firstchar,name,rank\
                    )VALUES (%s,%s,%s,%s\
                    )"
                    print(sql)
                    cursor.execute(sql,(a['code'],a['firstChar'],a['name'],a['rank']))
                    db.commit()  #提交数据
                    cursor.close()
        else:
            print('子元素为空')
    db.close()
def getcity():
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sqlExit = "select name,code from bosscity"
    res = cursor.execute(sqlExit)
    results = cursor.fetchall()
    for (i,j) in results:
        print(i,j)

def main():
    crawlcity()
    getcity()
    pass
if __name__ == '__main__':
    main()