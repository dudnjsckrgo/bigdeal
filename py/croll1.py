# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request

test_url=''

for url in test_url:
    handle = urllib.request.urlopen(url)
    data = handle.read()
    
    soup = BeautifulSoup(data,'html.parser')
    
    for img in soup.find_all("img"):
        print (img.get("src"))