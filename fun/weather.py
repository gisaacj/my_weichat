# -*- coding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
import re

def get_weather():
    weathers=[]
    url=''
    html=urllib.request.urlopen(url)
    bsObj = BeautifulSoup(html,"html.parser")
    weather=bsObj.findAll('div',{'class':'table_day15'})
    img=bsObj.findAll('img',{'class':'pngtqico'})
    for item,ite in zip(weather[:6],img[:6]):
        im=re.compile(r'src="(.*)" style').findall(str(ite))
        weathers.append(item.get_text().replace('\n','',3)[:-2])
        weathers.append(im[0])
    return weathers
