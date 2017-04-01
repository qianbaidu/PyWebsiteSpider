# -*- coding:utf-8 -*-
#python 2.7
#XiaoDeng
#http://tieba.baidu.com/p/2460150866
#标签操作


from bs4 import BeautifulSoup
import urllib
import re
import urllib2
import os

# #如果是网址，可以用这个办法来读取网页
# url = "http://tieba.baidu.com/p/2460150866"
# response = urllib2.urlopen(url)
# html = response.read()

def getByUrl(url):
    r = urllib2.Request(url)
    try:
        f = urllib2.urlopen(r, data=None, timeout=5)
        html =  f.read()
        return html
    except Exception,e:
        print(e)
        return ''

url = 'http://hardware-104.view.sitestar.cn/'
html = getByUrl(url)
soup = BeautifulSoup(html, 'html.parser')   #文档对象


#查找a标签,只会查找出一个a标签
#print(soup.a)#<a class="sister" href="http://example.com/elsie" id="xiaodeng"><!-- Elsie --></a>

# url = 'http://www.jb51.net/images/logo.gif'
# filename = os.path.basename(url)
# print(filename)
#
# sStr1 = 'default.css?v=14830804'
# print(sStr1[0:sStr1.find('?')])


dir = '/Applications/XAMPP/xamppfiles/htdocs/python/website/putOut'
for k in soup.find_all('link'):
    # print(k)
    # print(k['class'])#查a标签的class属性
    # print(k['id'])#查a标签的id值
    # print(k['href'])#查a标签的href值
    # print(k.string)#查a标签的string
    # #tag.get('calss')，也可以达到这个效果

    linkHref =  k['href']
    print(linkHref)
    linkFileName = os.path.basename(linkHref)
    if linkFileName.find('?') >= 0 :
        strNum = linkFileName.find('?')
        linkFileName = linkFileName[0:strNum]

    #判断路径是否绝对路径

    if linkHref.find('http') >= 0:
        print(linkHref)
        r = urllib2.Request(linkHref)
        try:
                f = urllib2.urlopen(r, data=None, timeout=5)
                result =  f.read()
                savePath = '%s/%s' % (dir,linkFileName)
                print(savePath)
                with open(savePath, 'w') as f:
                    f.write(result)
        except Exception,e:
                continue
    else:
        print '非绝对路径'
        pass
