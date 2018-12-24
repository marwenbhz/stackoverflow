# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from stackoverflow.items import StackoverflowItem


class StackoverflowspiderSpider(scrapy.Spider):
    name = 'stackoverflowspider'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['http://stackoverflow.com/questions?pagesize=50&sort=newest']
    #custom_settings = {
    #'LOG_FILE': 'logs/stackoverflow.log',
    #'LOG_LEVEL':'DEBUG'
     }
    #rules = [Rule(LinkExtractor(allow=r'questions\?page=[0-9]&sort=newest'),callback='parse', follow=True)]


    def parse(self, response):

        print('PROCESSING...' + response.url)

	questions = response.css('div.question-summary')
	for question in questions:

	    item = StackoverflowItem()

            try:
	        item['TITLE'] = question.css('a.question-hyperlink::text').extract_first().strip()
	    except:
		print('ERROR TITLE PARSE...' + response.url)
	    try:
		item['LIEN_QUESTION'] = response.urljoin(question.css('a.question-hyperlink::attr(href)').extract_first().strip())
	    except:
		print('ERROR LIEN QUESTION PARSE...' + response.url)
	    try:
		item['NBR_VOTES'] = question.css('span.vote-count-post > strong::text').extract_first()
            except:
		print('ERROR NBR_VOTES PARSE...' + response.url)
	    try:
	        item['NBR_VIEWS'] = question.css('div.views::text').extract_first().strip()
            except:
		print('ERROR NBR_VIEWS PARSE...' + response.url)
	    try:
		item['NBR_REPONSES'] = question.css('div.status > strong::text').extract_first()
	    except:
		print('ERROR NBR_REPONSES PARSE...' + response.url)
	    try:
                item['AUTHOR'] = question.css('div.user-details > a::text').extract_first().strip() if len(question.css('div.user-details > a::text').extract_first().strip()) != 0 else ' '
	    except:
                print('ERROR AUTHOR PARSE...' + response.url)
            try:
		item['AUTHOR_IMAGE'] = question.css('div.gravatar-wrapper-32 > img::attr(src)').extract_first().strip() if len(question.css('div.gravatar-wrapper-32 > img::attr(src)').extract_first().strip()) != 0 else ' '
	    except:
                print('ERROR AUTHOR IMAGE PARSE...' + response.url)
	    try:
		item['PUBLICATION_DATE'] = question.css('span.relativetime::text').extract_first().strip()
	    except:
                print('ERROR PUBLICATION DATE PARSE...' + response.url)

	    # Don't need to add description in our output, if you need description of question, just uncomment this code and uncomment description field in items.py.
	    #try:
		#item['DESCRIPTION'] = question.css('div.excerpt::text').extract_first().strip()
            #except:
                #print('ERROR DESCRIPTION PARSE...' + response.url)

	    try:
		item['TAGS'] = question.css('div.tags > a::text').extract()
	    except:
                print('ERROR TAGS PARSE...' + response.url)

	    yield item


	relative_next_url = response.xpath('//a[@rel="next"]/@href').extract_first()
	absolute_next_url = response.urljoin(relative_next_url)
	yield Request(absolute_next_url, callback=self.parse)

