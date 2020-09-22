# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:34:37 2019

@author: Administrator
"""
#scrapy shell
"""
fetch('http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001')
view(response)
print(response.text)
"""
#import twisted
import scrapy
#print sys.path

class NewsbotSpider(scrapy.Spider):
	name = 'newsbot'
	start_urls = ['http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001']

	def parse(self, response):
		titles = response.xpath('//*[@id="main_content"]/div[2]/ul[1]/li[4]/dl/dt[1]/a/text()').extract()
		authors = response.css('.writing::text').extract()
		previews = response.css('.lede::text').extract()

		for item in zip(titles, authors, previews):
			scraped_info = {
				'title' : item[0].strip(),
				'author' : item[1].strip(),
				'preview' : item[2].strip(),
			}
			yield scraped_info
