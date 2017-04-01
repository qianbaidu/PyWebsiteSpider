# -*- coding:utf-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup
import os
from urlparse import urljoin
import time
import random
import gzip
import StringIO
import chardet

class getHtml():
    def __init__(self):
        self.writeDir = '/Applications/XAMPP/xamppfiles/htdocs/python/website/putOut'
        self.fileType = ['css','js','swf','images','other']
        self.initFileArr()

    def initFileArr(self):
        # self.fileArr = []
        # for d in self.fileType:
        #     self.fileArr[d] = []
        self.cssFile    = []
        self.jsFile     = []
        self.imgFile    = []

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

    def tryGetUrl(self,url):
        print(url)
        user_agent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
            # 'Accept': '*/*',
            # 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            # 'Accept-Encoding': 'gzip, deflate',
        }
        r = urllib2.Request(url,None,user_agent)
        try:
            f = urllib2.urlopen(r, data=None, timeout=5)
            headers = f.info()
            html =  f.read()
            if ('Content-Encoding' in headers and headers['Content-Encoding']) or \
                ('content-encoding' in headers and headers['content-encoding']):
                data = StringIO.StringIO(html)
                gz = gzip.GzipFile(fileobj=data)
                html = gz.read()
                gz.close()
            return html
        except Exception,e:
            print(e)
            return ''

    def getByUrl(self,url):
        # html = ''
        html = self.tryGetUrl(url)
        # for i in range(5):
        #     html = self.tryGetUrl(url)
        #     adchar=chardet.detect(html)
        #     if adchar['encoding'] == None:
        #         for i in range(3):
        #             html = self.tryGetUrl(url)
        #             adchar=chardet.detect(html)
        #             print(adchar)
        #             if adchar['encoding'] != None:
        #                 break

        return html

    def putOutFile(self,savePath,content):
         with open(savePath, 'w') as f:
            if isinstance(content, unicode):
                content = content.encode('gb2312')
            else:
                pass
                #content = content.decode('utf-8')
            f.write(content)

    def saveCss(self,linkHref,savePath):
        fileType = ['.png','.jpg','.jpeg','.bmp','.gif','.svg','.htc','.eot','.woff2','.ttf','.woff','.css']
        if linkHref.find('http') < 0:
            linkHref = urljoin(self.url,linkHref)
        fileContent = self.getByUrl(linkHref)

        if len(fileContent) > 0:
            # 下载/替换 背景图 下载导入css
            backImg=re.findall(r"\(.*?\)",fileContent)
            for i in backImg:
                imgUrlPath = i.replace('(','').replace(')','')
                if imgUrlPath.find('?') >= 0 :
                    strNum = imgUrlPath.find('?')
                    imgUrlPath = imgUrlPath[0:strNum]

                imgUrl = os.path.split(imgUrlPath)

                # print(imgUrl)
                imgType = os.path.splitext(imgUrl[1])
                imgTypePro = imgType[1].replace("'",'').replace('"','')


                if imgTypePro not in fileType:
                    #print(imgType)
                    continue
                url = urljoin(linkHref,imgUrlPath)
                # print(imgUrl)
                #print(imgUrlPath)
                if(len(imgUrl[0]) > 0):
                    replaceDir = '%s/' % (imgUrl[0])
                    #print('11=> %s替换%s' % (replaceDir,'./images/'))
                    fileContent = fileContent.replace(replaceDir,'./images/')
                else:
                    replacePath = './images/%s' % imgUrlPath.replace("'",'')
                    #print('22=> %s替换%s' % (imgUrlPath,replacePath))
                    fileContent = fileContent.replace(imgUrlPath,replacePath)
                imgContent = self.getByUrl(url)
                if imgContent == '' or imgContent == None:
                    continue

                if len(imgContent) > 0 and len(imgUrl[1]) > 0:
                    saveImgDir = self.dir['css']+'/images'
                    saveImgPath = self.dir['css']+'/images/'+imgUrl[1]
                    # print(saveImgPath)
                    #print(saveImgDir)
                    #print(saveImgPath)
                    #print(os.path.exists(saveImgDir))
                    #print(len(imgContent))
                    if os.path.exists(saveImgDir) == False :
                        os.makedirs(saveImgDir)
                    self.putOutFile(saveImgPath,imgContent)
            #print(savePath)
            self.putOutFile(savePath,fileContent)

    def decode(self,code):
        if isinstance(code, unicode):
            #print(111)
            return code
            #return code.encode('gb2312')
        else:
            print(222)
            return code.decode('utf-8')
            #print code.decode('utf-8').encode('gb2312')

    def test(self,url):
        self.url = url
        html = self.getByUrl(url)
        #html = self.decode(html)

        if(len(html) > 0):
            #读取css js images 路径
            # soup = BeautifulSoup(html,from_encoding="utf8")
            soup = BeautifulSoup(html,'html.parser')
            #soup = BeautifulSoup(html, 'html5lib', from_encoding='utf8')

            # link css
            for linkUrl in soup.find_all("link"):
                linkHref =  linkUrl['href']
                if linkHref.find('http') < 0:
                    linkHref = urljoin(self.url,linkHref)
                linkFileName = os.path.basename(linkHref)
                if linkFileName.find('?') >= 0 :
                    strNum = linkFileName.find('?')
                    linkFileName = linkFileName[0:strNum]

                linkUrl['href'] = './css/%s' % (linkFileName)
                savePath = '%s/%s' % (self.dir['css'],linkFileName)
                #print(savePath)
                if linkFileName == '' or linkFileName == None:
                    continue
                if len(linkFileName) > 0  and len(linkFileName) > 0:
                    self.saveCss(linkHref,savePath)

            # import css
            for linkUrl in soup.find_all("link"):
                linkHref =  linkUrl['href']
                if linkHref.find('http') < 0:
                    linkHref = urljoin(self.url,linkHref)
                linkFileName = os.path.basename(linkHref)
                if linkFileName.find('?') >= 0 :
                    strNum = linkFileName.find('?')
                    linkFileName = linkFileName[0:strNum]

                linkUrl['href'] = './css/%s' % (linkFileName)
                savePath = '%s/%s' % (self.dir['css'],linkFileName)
                #print(savePath)
                if linkFileName == '' or linkFileName == None:
                    continue
                if len(linkFileName) > 0  and len(linkFileName) > 0:
                    self.saveCss(linkHref,savePath)

            # js
            jsArr =[]
            for jsSrc in soup.findAll("script", attrs={"src": True}):
                #print(jsSrc)
                jsUrl =  jsSrc['src']
                # print(jsUrl)
                jsFileName = os.path.basename(jsUrl)

                if jsFileName.find('?') >= 0 :
                    strNum = jsFileName.find('?')
                    jsFileName = jsFileName[0:strNum]
                # print(jsFileName)
                if jsUrl.find('http') < 0:
                    jsUrl = urljoin(self.url,jsUrl)
                fileContent = self.getByUrl(jsUrl)
                if jsFileName in self.jsFile:
                    jsFileName = '%d_%d_%s' % (time.time(),random.randint(1000,9999),jsFileName)
                self.jsFile.append(jsFileName)
                # jsArr.append(jsFileName)
                # print(jsArr)
                # print(self.jsFile)
                #self.jsFile.append[jsFileName]
                jsSrc['src'] = './js/%s' % (jsFileName)
                savePath = '%s/%s' % (self.dir['js'],jsFileName)
                print(savePath)




                if fileContent == '' or fileContent == None:
                    continue
                if len(fileContent) > 0 and len(jsFileName) > 0:
                    self.putOutFile(savePath,fileContent)



            # images
            for jsSrc in soup.findAll("img", attrs={"src": True}):
                # print(jsSrc)
                jsUrl =  jsSrc['src']
                jsFileName = os.path.basename(jsUrl)

                if jsFileName.find('?') >= 0 :
                    strNum = jsFileName.find('?')
                    jsFileName = jsFileName[0:strNum]
                # print(jsFileName)
                if jsUrl.find('http') < 0:
                    jsUrl = urljoin(self.url,jsUrl)
                fileContent = self.getByUrl(jsUrl)
                if jsFileName in self.jsFile:
                    jsFileName = '%d_%d_%s' % (time.time(),random.randint(1000,9999),jsFileName)
                self.jsFile.append(jsFileName)
                jsSrc['src'] = './images/%s' % (jsFileName)
                savePath = '%s/%s' % (self.dir['images'],jsFileName)
                # print(savePath)


                if fileContent == '' or fileContent == None:
                    continue
                if len(fileContent) > 0 and len(jsFileName) > 0:
                    self.putOutFile(savePath,fileContent)

            #图片懒加载
            for jsSrc in soup.findAll("img", attrs={"data-original": True}):
                # print(jsSrc)
                jsUrl =  jsSrc['data-original']
                # print(jsUrl)
                jsFileName = os.path.basename(jsUrl)

                if jsFileName.find('?') >= 0 :
                    strNum = jsFileName.find('?')
                    jsFileName = jsFileName[0:strNum]
                # print(jsFileName)
                fileContent = self.getByUrl(jsUrl)
                if jsFileName in self.jsFile:
                    jsFileName = '%d_%d_%s' % (time.time(),random.randint(1000,9999),jsFileName)
                self.jsFile.append(jsFileName)
                jsSrc['src'] = './images/%s' % (jsFileName)
                savePath = '%s/%s' % (self.dir['images'],jsFileName)
                # print(savePath)
                if jsUrl.find('http') < 0:
                    jsUrl = urljoin(self.url,jsUrl)

                if fileContent == '' or fileContent == None:
                    continue
                if len(fileContent) > 0 and len(jsFileName) > 0:
                    self.putOutFile(savePath,fileContent)


            indexSavePath = '%s/index.html' % (self.baseDir)
            indexContent = soup.prettify(encoding='utf-8',formatter="html")

            # print indexContent.decode('utf-8')
            # print(soup.prettify())
            # print(indexContent)
            self.putOutFile(indexSavePath,indexContent)

if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

    getHtml = getHtml()
    url = 'http://www.hejun.com.cn/'

    getHtml.initDir()
    getHtml.test(url)
