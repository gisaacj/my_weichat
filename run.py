# -*- coding: utf-8 -*-
import os
import web
import re
import json
import time
import datetime
import urllib.request
import hashlib
from lxml import etree
from main import text_resp,event_resp
from menu import menu

web.config.debug = False

my_appid = ''
my_secret = ''




def image_resp():
    pass

def voice_resp():
    pass

def video_resp():
    pass

def shortvideo_resp():
    pass

def location_resp():
    pass

def link_resp():
    pass




msg_type = {
    'text':text_resp,
    'image':image_resp,
    'voice':voice_resp,
    'video':video_resp,
    'shortvideo':shortvideo_resp,
    'location':location_resp,
    'link':link_resp,
    
'event':event_resp,
}

def check_hash(data):
    signature = data.signature
    timestamp = data.timestamp
    nonce = data.nonce
    echostr = data.echostr
    token = ''
    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    list2 = ''.join(list)
    sha1.update(list2.encode('utf-8'))
    hashcode = sha1.hexdigest()
    if hashcode == signature:
        return echostr


class WeixinInterface:

    def GET(self):
        data = web.input()
        if check_hash(data):
            return data.echostr

    def POST(self):
        str_xml = web.data()
        xml = etree.fromstring(str_xml)
        msgType = xml.find('MsgType').text
        response = msg_type[msgType](xml)
        return response


urls = (
    '/weixin','WeixinInterface',
    )


if __name__ == "__main__":
    menu.createmenu()
    app= web.application(urls,globals())
    app.run()

