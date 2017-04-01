#!/usr/bin/env python
# -*- coding:utf-8 -*-
s = '水壶'

if isinstance(s, unicode):
    #s=u"中文"
    print(111)
    print s.encode('gb2312')
else:
    #s="中文"
    print(222)
    print s.decode('utf-8')
    #print s.decode('utf-8').encode('gb2312')