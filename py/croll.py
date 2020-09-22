# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

res = requests.get('http://v.media.daum.net/v/20170615203441266')
#print(res.content)
soup = BeautifulSoup(res.content, 'html.parser')
title = soup.find('title')
print(title.get_text())