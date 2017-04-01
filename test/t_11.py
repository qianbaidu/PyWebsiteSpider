# -*- coding:utf-8 -*-
import urllib2
import gzip
import StringIO

url = 'http://guomeidiyicheng.soufun.com/xiangqing/'
data = urllib2.urlopen(url).read()
# data = StringIO.StringIO(data)
# gzipper = gzip.GzipFile(fileobj=data)
# html = gzipper.read()
print data