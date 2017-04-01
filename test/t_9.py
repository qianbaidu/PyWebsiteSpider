# -*- coding:utf-8 -*-
import urllib
rawdata = urllib.urlopen('http://www.cssmoban.com/min/?f=statics/css/styles.css').read()
import chardet
print chardet.detect(rawdata)
print(rawdata)
