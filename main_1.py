# -*- coding:utf-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup
import os

class getHtml():
    def __init__(self):
        self.writeDir = '/Applications/XAMPP/xamppfiles/htdocs/python/website/putOut'
        self.fileType = ['css','js','swf','images','other']


    def initDir(self,dir=None):
        if dir == None:
            dir = os.path.abspath('.')
            dir = '%s/putOut' % (dir)
            if os.path.exists(dir) == False :
                 os.makedirs(dir)
            self.baseDir = dir;
        self.dir = {}
        for d in self.fileType:
            tmpDir = '%s/%s' % (dir,d)
            if os.path.exists(tmpDir) == False :
                os.makedirs(tmpDir)
            self.dir[d] = tmpDir

    def getByUrl(self,url):
        user_agent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
        }
        r = urllib2.Request(url,None,user_agent)
        try:
            f = urllib2.urlopen(r, data=None, timeout=5)
            html =  f.read()
            return html
        except Exception,e:
            print(e)
            return ''

    def putOutFile(self,savePath,content):
         with open(savePath, 'w') as f:
            f.write(content)

    def test(self,url):
        self.url = url
        html = self.getByUrl(url)

        if(len(html) > 0):
            #读取css js images 路径
            # soup = BeautifulSoup(html,from_encoding="utf8")
            soup = BeautifulSoup(html,'html.parser')
            #soup = BeautifulSoup(html, 'html5lib', from_encoding='utf8')

            # css
            for linkUrl in soup.find_all("link"):
                linkHref =  linkUrl['href']

                linkFileName = os.path.basename(linkHref)
                if linkFileName.find('?') >= 0 :
                    strNum = linkFileName.find('?')
                    linkFileName = linkFileName[0:strNum]
                linkUrl['href'] = './css/%s' % (linkFileName)
                savePath = '%s/%s' % (self.dir['css'],linkFileName)
                #print(savePath)
                if linkHref.find('http') >= 0:
                    fileContent = self.getByUrl(linkHref)
                    if len(fileContent) > 0:
                        self.putOutFile(savePath,fileContent)
                else:
                    print(linkHref)

            # js
            for jsSrc in soup.findAll("script", attrs={"src": True}):
                # print(jsSrc)
                jsUrl =  jsSrc['src']
                # print(jsUrl)
                jsFileName = os.path.basename(jsUrl)

                if jsFileName.find('?') >= 0 :
                    strNum = jsFileName.find('?')
                    jsFileName = jsFileName[0:strNum]
                # print(jsFileName)
                jsSrc['src'] = './js/%s' % (jsFileName)
                savePath = '%s/%s' % (self.dir['js'],jsFileName)
                # print(savePath)
                if jsUrl.find('http') >= 0:
                    fileContent = self.getByUrl(jsUrl)
                    if len(fileContent) > 0:
                        self.putOutFile(savePath,fileContent)
                else:
                    print(jsUrl)


            # images
            for jsSrc in soup.findAll("img", attrs={"src": True}):
                # print(jsSrc)
                jsUrl =  jsSrc['src']
                # print(jsUrl)
                jsFileName = os.path.basename(jsUrl)

                if jsFileName.find('?') >= 0 :
                    strNum = jsFileName.find('?')
                    jsFileName = jsFileName[0:strNum]
                # print(jsFileName)
                jsSrc['src'] = './images/%s' % (jsFileName)
                savePath = '%s/%s' % (self.dir['images'],jsFileName)
                # print(savePath)
                if jsUrl.find('http') >= 0:
                    fileContent = self.getByUrl(jsUrl)
                    if len(fileContent) > 0:
                        self.putOutFile(savePath,fileContent)
                else:
                    print(jsUrl)

            indexSavePath = '%s/index.html' % (self.baseDir)
            indexContent = soup.prettify(formatter="html")

            # print indexContent.decode('utf-8')
            # print(soup.prettify())
            print(indexContent)
            self.putOutFile(indexSavePath,indexContent)
            # print(indexSavePath)

if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

    getHtml = getHtml()
    url = 'http://hardware-104.view.sitestar.cn/'

    getHtml.initDir()
    getHtml.test(url)
