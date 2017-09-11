# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import json

def reword(word):
    datas={
        'key':'',
        'info':word
           }
    datas=urllib.parse.urlencode(datas).encode('utf-8')
    html=urllib.request.urlopen('http://www.tuling123.com/openapi/api',data=datas)
    info=json.loads(html.read().decode('utf-8'))
    return(info['text'])

