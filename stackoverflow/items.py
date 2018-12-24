# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StackoverflowItem(scrapy.Item):
    # define the fields for your item here like:
    NBR_VOTES = scrapy.Field()
    NBR_REPONSES = scrapy.Field()
    TITLE = scrapy.Field()
    NBR_VIEWS = scrapy.Field()
    AUTHOR = scrapy.Field()
    PUBLICATION_DATE = scrapy.Field()
    LIEN_QUESTION = scrapy.Field()
    #DESCRIPTION = scrapy.Field()
    TAGS = scrapy.Field()
    AUTHOR_IMAGE = scrapy.Field()
