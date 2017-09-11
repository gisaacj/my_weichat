# -*- coding: utf-8 -*-

def send_text(touser,fromuser,time,content):
    text = """<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
</xml>"""
    return (text % (touser,fromuser,time,content))


def send_pic(touser,fromuser,time,pic_url):
    pic = """<xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[%s]]></MediaId>
        </Image>
        </xml>"""
    return (pic % (touser,fromuser,time,pic_url))

def send_voice(touser,fromuser,time,media_id):
    voice = """<xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[voice]]></MsgType>
        <Voice>
        <MediaId><![CDATA[media_id]]></MediaId>
        </Voice>
        </xml>"""
    return (voice % (touser,fromuser,time,media_id))

def send_video(touser,fromuser,time,media_id,title,desc):
    video = """<xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[video]]></MsgType>
        <Video>
        <MediaId><![CDATA[%s]]></MediaId>
        <Title><![CDATA[%s]]></Title>
        <Description><![CDATA[%s]]></Description>
        </Video> 
        </xml>"""
    return (video % (touser,fromuser,time,media_id,title,desc))

def send_music(touser,fromuser,time,title,desc,music_url,hqmusicurl,thumbmediaid):
    music = """<xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[music]]></MsgType>
        <Music>
        <Title><![CDATA[%s]]></Title>
        <Description><![CDATA[%s]]></Description>
        <MusicUrl><![CDATA[%s]]></MusicUrl>
        <HQMusicUrl><![CDATA[%s]]></HQMusicUrl>
        <ThumbMediaId><![CDATA[%s]]></ThumbMediaId>
        </Music>
        </xml>"""
    return (music % (touser,fromuser,time,title,desc,music_url,hqmusicurl,thumbmediaid))

def send_txtpic(touser,fromuser,time,title0,desc0,pic_url0,url0,title1,desc1,pic_url1,url1):
    txtpic = """<xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[news]]></MsgType>
        <ArticleCount>2</ArticleCount>
        <Articles>
        <item>
        <Title><![CDATA[%s]]></Title> 
        <Description><![CDATA[%s]]></Description>
        <PicUrl><![CDATA[%s]]></PicUrl>
        <Url><![CDATA[%s]]></Url>
        </item>
        <item>
        <Title><![CDATA[%s]]></Title>
        <Description><![CDATA[%s]]></Description>
        <PicUrl><![CDATA[%s]]></PicUrl>
        <Url><![CDATA[%s]]></Url>
        </item>
        </Articles>
        </xml>"""
    return (txtpic % (touser,fromuser,time,title0,desc0,pic_url0,url0,title1,desc1,pic_url1,url1))


def send_weather(toUser,fromUser,createTime,day0,day1,day2,day3,day4,day5):
    txtwea="""<xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[news]]></MsgType>
        <ArticleCount>4</ArticleCount>
        <Articles>
        <item>
        <Title><![CDATA[武汉近三天天气]]></Title> 
        <Description><![CDATA[]]></Description>
        <PicUrl><![CDATA[http://img.ivsky.com/img/tupian/pre/201504/05/rainbow-005.jpg]]></PicUrl>
        <Url><![CDATA[]]></Url>
        </item>
        <item>
        <Title><![CDATA[%s]]></Title> 
        <Description><![CDATA[]]></Description>
        <PicUrl><![CDATA[%s]]></PicUrl>
        <Url><![CDATA[]]></Url>
        </item>
        <item>
        <Title><![CDATA[%s]]></Title> 
        <Description><![CDATA[]]></Description>
        <PicUrl><![CDATA[%s]]></PicUrl>
        <Url><![CDATA[]]></Url>
        </item>
        <item>
        <Title><![CDATA[%s]]></Title> 
        <Description><![CDATA[]]></Description>
        <PicUrl><![CDATA[%s]]></PicUrl>
        <Url><![CDATA[]]></Url>
        </item>
        </Articles>
        </xml>"""
    return (txtwea % (toUser,fromUser,createTime,day0,day1,day2,day3,day4,day5))
