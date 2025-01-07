# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import scrapy.item


class ScrapesamehadaItem(scrapy.Item):
    # define the fields for your item here like:
    animes = scrapy.Field()
    # pass


class AnimesItems(scrapy.Item):
    title = scrapy.Field()
    detail = scrapy.Field()
    # linkDownload = scrapy.Field()
    # url = scrapy.Field()
    # relesed = scrapy.Field()
    # link = scrapy.Field()
    # thumbnail = scrapy.Field()
    # posted = scrapy.Field()
    # links = scrapy.Field()

class AnimeEps(scrapy.Item):
    # title = scrapy.Field()
    episodes = scrapy.Field()
    
