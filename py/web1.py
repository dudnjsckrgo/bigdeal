# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:38:45 2019

@author: yyw
"""

from http import cookiejar
import urllib.request
import urllib.parse

cj= cookiejar.CookieJar()
cookie_handler = urllib.request.HTTPCookieProcessor(cj)
opener= urllib.request.build_opener(cookie_handler)
urllib.request.install_opener(opener)

def my_request(url, postfields):
    headers ={'User-agent':'Mozilla/4.0(compatible; MSIE 55.5;Windows NT)'}
    req= urllib.request.Request(url,postfields, headers)
    response = urllib.request.urlopen(req)
    return response
def login(username, passward):
    login_url = "https://world.taobao.com/markets/all/login?spm=a21wu.241046-kr.7607074463.12.41cab6cbbtolSx"
    form_values = {"id":"", "pw":""}
    formdata =urllib.parse.urlencode(form_values)
    
    try:
        response = my_request(login_url, formdata.encode())
    except IOError as e:
        print('We failed to open "%s".' % login_url)
    if hasattr(e,'code')
response = urllib.request.urlopen(req)
html = response.read()
