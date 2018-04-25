import urllib.request
from bs4 import BeautifulSoup  
import csv   
import socket
import time

temp=[]
def testDL(ipstr):
    proxy= urllib.request.ProxyHandler({'http':"{}:{}".format(ipstr[1], ipstr[2])})
    opener=urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    try:
        testUrl = 'http://httpbin.org/ip'
        testUrl = 'http://2017.ip138.com/ic.asp'
        req=urllib.request.Request(testUrl)
        res=urllib.request.urlopen(req).read()
        print("********************* √ {}    -- {}".format(ipstr, res))
        print(res,ipstr)
    except Exception as e:
        print("******** ×, {} -- {}".format(ipstr, e))
    time.sleep(1)

def IPpool(tds1,tds2):
    IpResult=''
    socket.setdefaulttimeout(2)
    proxy=tds1+':'+tds2 
    print(proxy)
    proxy_handler=urllib.request.ProxyHandler({"http":proxy})  
    opener=urllib.request.build_opener(proxy_handler)  
    urllib.request.install_opener(opener)  
    try:  
        html=urllib.request.urlopen('http://www.baidu.com')  
        IpResult = proxy
    except Exception:  
        print('E')
    return IpResult
 
def IPspider(numpage): 
    global temp 
    url='http://www.xicidaili.com/nn/'  
    user_agent='IP'  
    headers={'User-agent':user_agent}  
    for num in range(1,numpage+1):  
        ipurl=url+str(num)  
        print('Now downloading the '+str(num*100)+' ips')  
        request=urllib.request.Request(ipurl,headers=headers)  
        content=urllib.request.urlopen(request).read()  
        bs=BeautifulSoup(content,'html.parser')  
        res=bs.find_all('tr') 
        for item in res:  
            try:    
                tds=item.find_all('td')
                print("'http':'http://"+tds[1].text+":"+tds[2].text+"',")
            except IndexError:  
                    pass 

IPspider(10) 
              

