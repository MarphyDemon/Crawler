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
def getSub(results):
    # print(results['subLevelModelList'],num,"lidongd9ngdong1")
    db = pymysql.connect(**config)
    # for i in results:
    #     cursor = db.cursor()
    #     # print(results['code'],"aaaaaaaa")
    #     sqlExit = "select code from post where code = '%s'" % (i['code'])
    #     res = cursor.execute(sqlExit)
    #     if res:
    #         print('数据已存在', res)
    #         cursor.close()
    #     else:
    #         sql = "insert into post(code,firstChar,name,rank\
    #         )VALUES (%s,%s,%s,%s\
    #         )"
    #         cursor.execute(sql,(i['code'],i['firstChar'],i['name'],i['rank']))
    #         db.commit()  #提交数据
    #         cursor.close()
    #         # print("12121")
    #         if(i['subLevelModelList']):
    #             # print(results['subLevelModelList'],num,"lidongd9ngdong3")
    #             getSub(i['subLevelModelList'])
    #             # print(results['subLevelModelList'],num,"lidongd9ngdong")
    #             # print("0000")
    #         else:
    #             print('保存完成')
    # db.close()
    for i in results:
        cursor = db.cursor()
        # print(results['code'],"aaaaaaaa")
        sqlExit = "select code from post where code = '%s'" % (i['code'])
        res = cursor.execute(sqlExit)
        if res:
            print('数据已存在', res)
            cursor.close()
        else:
            sql = "insert into post(code,firstChar,name,rank,grade\
            )VALUES (%s,%s,%s,%s,%s\
            )"
            cursor.execute(sql,(i['code'],i['firstChar'],i['name'],i['rank'],1))
            db.commit()  #提交数据
            cursor.close()
            # print("12121")
            if(i['subLevelModelList']):
                for a in i['subLevelModelList']:
                    cursor = db.cursor()
                    # print(results['code'],"aaaaaaaa")
                    sqlExit = "select code from post where code = '%s'" % (a['code'])
                    res = cursor.execute(sqlExit)
                    if res:
                        print('数据已存在', res)
                        cursor.close()
                    else:
                        sql = "insert into post(code,firstChar,name,rank,grade\
                        )VALUES (%s,%s,%s,%s,%s\
                        )"
                        cursor.execute(sql,(a['code'],a['firstChar'],a['name'],a['rank'],2))
                        db.commit()  #提交数据
                        cursor.close()
                        # print("12121")
                        if(a['subLevelModelList']):
                            for b in a['subLevelModelList']:
                                cursor = db.cursor()
                                # print(results['code'],"aaaaaaaa")
                                sqlExit = "select code from post where code = '%s'" % (b['code'])
                                res = cursor.execute(sqlExit)
                                if res:
                                    print('数据已存在', res)
                                    cursor.close()
                                else:
                                    sql = "insert into post(code,firstChar,name,rank,grade\
                                    )VALUES (%s,%s,%s,%s,%s\
                                    )"
                                    cursor.execute(sql,(b['code'],b['firstChar'],b['name'],b['rank'],3))
                                    db.commit()  #提交数据
                                    cursor.close()
                                    # print("12121")
                # print(results['subLevelModelList'],num,"lidongd9ngdong3")
                # getSub(i['subLevelModelList'])
                # print(results['subLevelModelList'],num,"lidongd9ngdong")
                # print("0000")
            else:
                print('保存完成')
    db.close()

def crawlcity():
    headers = {'Referer':'https://www.zhipin.com/common/data/position.json',               'Origin':'https://www.zhipin.com',                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
               'Accept':'application/json, text/javascript, */*; q=0.01',
               'Cookie':'JSESSIONID=""; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1520823369,1520823381,1522231558; __c=1522231566; __l=r=https%3A%2F%2Fwww.zhipin.com%2F&l=%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3D%26scity%3D101010100%26industry%3D%26position%3D; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fjob_detail%2F1418574492.html%3Fka%3Dsearch_list_1; lastCity=101020100; __a=52508175.1522231554.1522231554.1522231566.48.2.47.48; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1522242845'
               }
    url='https://www.zhipin.com/common/data/position.json'
    resp = requests.post(url,headers=headers)
    results = resp.json()['data']
    getSub(results)
        
            # if(i['subLevelModelList']):
            #     for a in i['subLevelModelList']:
            #         cursor = db.cursor()
            #         sqlExit = "select code from position where code = '%s'" % (a['code'])
            #         res = cursor.execute(sqlExit)
            #         if res:
            #             print('数据已存在', res)
            #             cursor.close()
            #         else:
            #             sql = "insert into position(code,firstChar,name,rank\
            #             )VALUES (%s,%s,%s,%s\
            #             )"
            #             print(sql)
            #             cursor.execute(sql,(a['code'],2,a['name'],a['rank']))
            #             db.commit()  #提交数据
            #             cursor.close()
            #             if(a['subLevelModelList']):
            #                 for b in a['subLevelModelList']:
            #                     cursortwo = db.cursor()
            #                     sqlExittwo = "select code from position where code = '%s'" % (a['code'])
            #                     restwo = cursortwo.execute(sqlExittwo)
            #                     if restwo:
            #                         print('数据已存在', restwo)
            #                         cursortwo.close()
            #                     else:
            #                         sqltwo = "insert into position(code,firstChar,name,rank\
            #                         )VALUES (%s,%s,%s,%s\
            #                         )"
            #                         print(sqltwo)
            #                         cursortwo.execute(sqltwo,(b['code'],3,b['name'],b['rank']))
            #                         db.commit()  #提交数据
            #                         cursortwo.close()
            #             else
            # else:
                # print('子元素为空')
    # db.close()
def getcity():
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sqlExit = "select name from post"
    res = cursor.execute(sqlExit)
    results = cursor.fetchall()
    for (i,) in results:
        print(i)

def main():
    crawlcity()
    getcity()
    pass
#输入你想要爬取的职位名,如:python
if __name__ == '__main__':
    main()