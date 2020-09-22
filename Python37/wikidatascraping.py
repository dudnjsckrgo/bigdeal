import csv
import urllib.request
from bs4 import BeautifulSoup
f = open('dataoutput.csv','w', newline='')
writer =csv.writer(f)

soup = BeautifulSoup(urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_largest_recorded_music_markets").read(), 'lxml')

tbody = soup('table' ,{"class":"wikitable plainrowheaders sortable"})[0].find_all('tr')
for row in tbody:
        cols = row.findChildren(recursive=False)
        cols = [ele.text.strip() for ele in cols]
        writer.writerow(cols)
        print(cols)
