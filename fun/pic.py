# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import json

def repic(url):
    datas={
        'api_key':'',
        'api_secret':'',
        'image_url':url
        }
    datas=urllib.parse.urlencode(datas).encode('utf-8')
    html=urllib.request.urlopen('https://api-cn.faceplusplus.com/imagepp/beta/detectsceneandobject',data=datas)
    info=json.loads(html.read().decode('utf-8'))
    return info['objects']
