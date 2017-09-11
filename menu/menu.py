# -*- coding: utf-8 -*-

import urllib.request
import json

my_appid = ''
my_secret = ''

def gettoken():
    html=urllib.request.urlopen('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' %(my_appid,my_secret))
    data=html.read().decode('utf-8')
    jsdata=json.loads(data)
    access_token = jsdata.get('access_token',None)
    if access_token == None:
        gettoken()
    html.close()
    return access_token

def createmenu():
    postData=r"""
{
        "button":
        [
            {
                "type": "click",
                "name": "武汉天气",
                "key":  "weather"
            },
            {
                "name": "图书管理",
                "sub_button":
                [
                    {
                        "type": "click",
                        "name": "我要推荐",
                        "key": "recommend"
                    },
                    {
                        "type": "click",
                        "name": "京东热销",
                        "key": "jd"
                    },
                    {
                        "type": "click",
                        "name": "我要借书",
                        "key": "js"
                    },
                    {
                        "type": "click",
                        "name": "已借书目",
                        "key": "yj"
                    }
                ]
            },
            {
                "type": "view",
                "name": "报名平台",
                "url": ""
            },
          ]
    }
    """
    postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % gettoken()
    if isinstance(postData,str):
        postData = postData.encode('utf-8')
    urlResp = urllib.request.urlopen(url=postUrl,data=postData)
    data = urlResp.read()
    data = data.decode('utf-8')
