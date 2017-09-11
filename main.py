# -*- coding:utf8 -*-
import time
import re
from response import send_text,send_music,send_pic,send_txtpic,send_video,send_voice,send_weather
from fun import weather,chat,jdbook,js,pic
import oop

def cancel_command(xml):
    User=oop.read_user()
    fromUser = xml.find('FromUserName').text
    toUser = xml.find('ToUserName').text
    if fromUser in User and User[fromUser] != 'default':
        User[fromUser] = 'default'
        oop.save_user(User)
        reply = send_text(fromUser, toUser, int(time.time()), '已退出该模式')
        return reply
    else:
        reply = send_text(fromUser, toUser, int(time.time()), '未在任何模式中')
        return reply

def fweather(xml):
    fromUser = xml.find('FromUserName').text
    toUser = xml.find('ToUserName').text
    days=weather.get_weather()
    reply = send_weather(fromUser,toUser,int(time.time()),days[0],days[1],days[2],days[5],days[4],days[9])
    return reply


def register(xml):
    fromUser = xml.find('FromUserName').text
    toUser = xml.find('ToUserName').text
    reply = send_text(fromUser, toUser, int(time.time()), '不会点菜单吗')
    return reply

def other(xml):
    fromUser = xml.find('FromUserName').text
    toUser = xml.find('ToUserName').text
    reply = send_text(fromUser, toUser, int(time.time()), '喵喵喵？')
    return reply

def test(xml):
    fromUser = xml.find('FromUserName').text
    toUser = xml.find('ToUserName').text
    content = xml.find('Content').text
    if content == '取消':
        reply=cancel_command(xml)
    else:
        User=oop.read_user()
        User[fromUser] = 'default'
        oop.save_user(User)
        reply = send_text(fromUser, toUser, int(time.time()), '测试完成')
    return reply

def chat_robot(xml):
    content = xml.find('Content').text
    fromUser = xml.find('FromUserName').text
    toUser = xml.find('ToUserName').text
    reply = chat.reword(content)
    reply = send_text(fromUser,toUser,int(time.time()),reply)
    return reply

def enter_test(xml):
    fromUser = xml.find('FromUserName').text
    toUser = xml.find('ToUserName').text
    User=oop.read_user()
    User[fromUser] = 'test'
    oop.save_user(User)
    reply = send_text(fromUser,toUser,int(time.time()),'进入测试阶段')
    return reply

def show_menu(xml):
    fromUser = xml.find('FromUserName').text
    toUser = xml.find('ToUserName').text
    reply = send_text(fromUser, toUser, int(time.time()), '菜单/取消/天气/报名/其他/测试')
    return reply


def text_resp(xml):
    User=oop.read_user()
    print(User)
    content = xml.find('Content').text
    fromUser = xml.find('FromUserName').text
    content = content.replace(u'　', ' ')
    content = content.lstrip()
    commands = {
        '菜单': show_menu,
        '取消': cancel_command,
        '天气': fweather,
        '报名': register,
        '其他': other,
        '测试': enter_test,
    }
    states = {
        'default': chat_robot,
        'test': test,
    }

    command_match = False
    for key_word in commands:
        if User[fromUser] != 'default':
            break
        if re.match(key_word, content):
            response = commands[key_word](xml)
            command_match = True
            break
    if not command_match:
        # 匹配状态
        state = User[fromUser]
        # 关键词、状态都不匹配，缺省回复
        if state == 'default' or not state:
            response = chat_robot(xml)
        else:
            response = states[state](xml)
    return response

def event_resp(xml):
    Event=xml.find('Event').text
    EventKey=xml.find('EventKey').text
    if Event=='CLICK':
        if EventKey=='weather':
            response=fweather(xml)
            return response
    
