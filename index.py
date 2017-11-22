#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, simplejson,unicodedata
import sys

reload(sys)
sys.setdefaultencoding('utf8')

url = "http://iiif.nli.org.il/collections/root.json"

rootPage = simplejson.loads(urllib.urlopen(url).read())
collections = rootPage['collections']

for collection in collections:
    urlLibrary = collection['@id']
    # print urlLibrary
    librariesPage = simplejson.loads((urllib.urlopen(urlLibrary).read()))
    urlImages = librariesPage['members']
    for urlImg in urlImages:
        print urlImg
        imgStr = (urllib.urlopen(urlImg['@id']).read()).decode('utf-8').encode('utf-8')
        imgPage = simplejson.loads(imgStr)
        print imgPage
