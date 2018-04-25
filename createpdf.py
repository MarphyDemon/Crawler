from reportlab.pdfgen import canvas  
from reportlab.platypus import Paragraph,PageTemplate
from reportlab.lib.pagesizes import letter, A4  
from reportlab.platypus import Image as platImage  
from PIL import Image  
import time
from reportlab.lib import colors  
from reportlab.pdfbase.ttfonts import TTFont  
from reportlab.pdfbase import pdfmetrics 
from reportlab.platypus.doctemplate import BaseDocTemplate, Frame
from reportlab.lib.units import cm,inch
from reportlab.lib.styles import getSampleStyleSheet
import os

def cPdf():
    body={}
    # username = request.POST.get('Menuname',None)
    # positionName = request.POST.get('positionName',None)
    createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    #支持中文，需要下载相应的文泉驿中文字体  
    pdfmetrics.registerFont(TTFont('hei', 'wqy-zenhei.ttc'))   
    #设置页面大小  
    c = canvas.Canvas('测试.pdf',pagesize=A4)  
    xlength,ylength = A4  
    print('width:%d high:%d'%(xlength,ylength))  
    #设置文字类型及字号  
    c.setFont('hei',10)  
    #生成一个table表格   
    textOb = c.beginText()
    textStr = '''''test 中文写入测试中文写入测试中文写入测试中文写入测试'''
    #print('nextline,nextline%d'%indexVlaue)  
    textOb.textLine(textStr)  
    c.drawText(textOb)  
    #简单的图片载入  
    c.showPage()  
    #换页的方式不同的showPage  
    c.drawString(0,0,'helloword322ew')  
    c.showPage()  
    c.save()  

cPdf()
