#https://www.youtube.com/watch?v=K1xVFqT4sqY
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import win32com.client


#Get our Excel Application
ExcelApp = win32com.client.gencache.EnsureDispatch("Excel.Application")

#Get our worksheet
WrkSht = ExcelApp.ActiveSheet

#define our range of URLS
Url_List = WrkSht.Range("A1:C1").Value

#definr a section initalizer
section_init=1

#loop through each url in our Url_list
for url in Url_List[0]:

#request the url, and initalize the list that will store the links
        req = Request(url)
        html_page = urlopen(req)
        column_list =[]
#get the HTML cent
soup =BeautifulSoup(html_page, 'html.parser')

#Loop through ech "a" tag, grab the link and store it in the link
for link in soup.findAll('a'):
        row_list = []
        row_list.append(link.get('href'))
        column_list.append(row_list)

#dump the urls in the proper section
        StartCell = WrkSht.Cells(2,section_init)
        EndCell =WrkSht.Cells(2 + len(column_list), section_init)
        ExcelApp.Range(StartCell, EndCell).Value =column_list

        #mark sure to increment our initalizer
        section_init +=1
        
