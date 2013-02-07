#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pickle
import urllib

URL = "http://www.pythonchallenge.com/pc/def/banner.p"

datastream = urllib.urlopen(URL)
obj = pickle.load(datastream)
for o in obj:
    s = ""
    for ch, n in o:
        s = "%s%s" % (s, ch * n)
    print s

