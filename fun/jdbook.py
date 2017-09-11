# -*- coding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
import re

def getinfo(choice):
    url='http://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10001-1#comfort'
    html=urllib.request.urlopen(url)
    bsObj = BeautifulSoup(html,"html.parser")
    books=bsObj.findAll('li')
    bimg=[]
    bauthor=[]
    bname=[]
    bpublish=[]

    for x in books[34:44]:
        imgs=str(x.find('img'))
        details=x.find('div',{'class':'p-detail'})
        bookname=details.find('a',{'class':'p-name'}).get_text()
        author=details.find('dl').get_text().replace(' ','').replace('\n','')
        publishes=details.findAll('dl')
        publish=publishes[1].get_text().replace(' ','').replace('\n','')
        img=re.compile(r'data-lazy-img="(.*)" height').findall(imgs)
        bimg.append(img[0])
        bauthor.append(author)
        bname.append(bookname)
        bpublish.append(publish)
    if choice=='img':
        return bimg
    if choice=='author':
        return bauthor
    if choice=='publish':
        return bpublish
    if choice=='name':
        return bname
