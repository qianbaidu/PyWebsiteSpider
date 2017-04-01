#!/usr/bin/python
#coding=utf-8

import re
from urlparse import urljoin
#写一个正则表达式，能匹配出多种格式的电话号码，包括
#(021)88776543   010-55667890 02584453362  0571 66345673
#\(?0\d{2,3}[) -]?\d{7,8}
import re
text="(021)88776543 010-55667890 02584533622 057184720483 837922740"
m=re.findall(r"\(?0\d{2,3}[) -]?\d{7,8}",text)
if m:
    print m
else:
    print 'not match'

css = '''
.wp-new-member-login-windows-top{ height:35px; background:url(../images/wp-new-member-background.png) no-repeat 0 -32px;}
.wp-new-member-login-windows-c{ background:url(../images/wp-new-member-login-windows-c.png) repeat-y; padding:5px 35px 24px 35px;}
.wp-new-member-login-windows-bottom{ height:45px; background:url(../images/wp-new-member-background.png) no-repeat 0 -68px;}
.wp-new-member-close{ width:30px; height:29px; position:absolute; z-index:100; margin:10px 0 0 500px;}
.wp-new-member-close a{ display:block; width:30px; height:29px; background:url(../images/wp-new-member-background.png) no-repeat;}
.wp-new-member-close a:hover{ background-position:-32px 0;}
'''
url = '"http://static.websiteonline.cn/website/template/default/css/'
m=re.findall(r"\(.*?\.(png|jpg|jpeg|bmp|gif|svg|htc|eot|woff2|ttf)\)",css)
print(m)
# for i in m:
    # print(i)
    # count = i.count('../')
    # str = '/..' * count

    # urlstr = i.replace('(','').replace(')','')
    # print(urlstr)
    # print(urljoin(url,urlstr))
    # print(i.count('../'))
    # print(i.replace('(','').replace(')','').replace('../','').replace('./',''))
# print(m)


# s = "Count, the number of spaces."
# print s.count(" ")
# x = "I like to program in Python"
# print x.count("i")


# import os
#
# dir = os.path.abspath('.')
# print(dir)
# print(os.path.abspath(dir))
# print(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
# print os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
#
#
# import sys
# pwd = sys.path[0]    # 获取当前执行脚本的位置
# print os.path.abspath(os.path.join(pwd))