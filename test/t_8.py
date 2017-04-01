# -*- coding:utf-8 -*-
import urllib2
import chardet
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

def getByUrl(url):
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
        # 'Accept': '*/*',
        # 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate',
    }
    r = urllib2.Request(url,None,user_agent)
    try:
        f = urllib2.urlopen(r, data=None, timeout=5)
        html =  f.read()
        return html
    except Exception,e:
        print(e)
        return ''


# fileContent = getByUrl('http://www.cssmoban.com/min/?f=statics/css/styles.css')
fileContent = getByUrl('http://www.cssmoban.com/')

adchar=chardet.detect(fileContent)
if adchar['encoding'] == None:
    for i in range(3):
        fileContent = getByUrl('http://www.cssmoban.com/min/?f=statics/css/styles.css')
        adchar=chardet.detect(fileContent)
        if adchar['encoding'] != None:
            break
print(fileContent)
print adchar


# if adchar['encoding']=='utf-8':
#     fileContent=fileContent.decode('utf-8')
# else:
#     fileContent=fileContent.decode('gbk')
# print(fileContent)
