# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:08:41 2019

@author: Administrator
"""
import requests
 
URL = "https://item.taobao.com/item.htm?spm=a21wu.241046-kr.4691948847.3.41cab6cbStMoqe&scm=1007.15423.84311.100200300000001&id=38314803256&pvid=ea566e79-39fa-450a-9710-f66aea9b5121"
#url = "https://www.test.com"
#rs = requests.post(url,auth=("skyutech","sky4275"))
headers = {'Content-Type': 'application/json; charset=utf-8'} 
cookies = {'session_id': 'sorryidontcare'} 
rs = requests.get(URL, headers=headers, cookies=cookies)
# response code

rs_code = rs.status_code
 
if int(rs_code) == 200 :
    print("Okay")
    rs_text = rs.text
    print(rs_text)
else :
    print(rs_code)
    print("Fail")
