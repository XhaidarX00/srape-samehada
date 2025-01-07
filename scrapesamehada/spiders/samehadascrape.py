from typing import Any, Iterable
import scrapy
from scrapy.http import Response
from ..items import AnimesItems, ScrapesamehadaItem, AnimeEps
import asyncio

# preceding-sibling:: => untuk mengambil data saudara sebelumnya
# following-sibling:: => untuk mengambil data setelahnya

import requests
from urllib.parse import urlencode


class ScrapesamehadaspiderSpider(scrapy.Spider):
    name = "animespider"
    allowed_domains = ["samehadaku.email", "api.scraperapi.com", "proxy.scrapeops.io"]
    start_urls = ["https://samehadaku.email/daftar-anime-2/?list"]
    
    custom_settings = {
        'FEEDS' : {
            'animes.json': {'format': 'json', 'overwrite': True},
        },
        'DOWNLOADER_MIDDLEWARES': {
            "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
            "scrapy.downloadermiddlewares.retry.RetryMiddleware": None,
            "scrapy_fake_useragent.middleware.RandomUserAgentMiddleware": 400,
            "scrapy_fake_useragent.middleware.RetryUserAgentMiddleware": 401,
        },
        'FAKEUSERAGENT_PROVIDERS': [
            "scrapy_fake_useragent.providers.FakerProvider",
            "scrapy_fake_useragent.providers.FakeUserAgentProvider",
            "scrapy_fake_useragent.providers.FixedUserAgentProvider",
        ],
    }
    
    datas = ScrapesamehadaItem()
    anime_items = AnimesItems()
    anime_eps = AnimeEps()
    
    
    # def scrape_proxy(self, url):
    #     payload = {'api_key': '4f34e77e2abd70ac72f7e3', 'url': url}
    #     proxy_url = 'https://api.scraperapi.com/?' + urlencode(payload)
    #     return proxy_url

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)
        # yield scrapy.Request(url=self.scrape_proxy(self.start_urls[0]), callback=self.parse)
        
    
    def parse(self, response):
        try:
            animes = response.css('div.listbar div.listttl ul li')
            # animes = response.xpath('//div[@name="#"]/div[@class="listttl"]/ul/li')
        except:
            animes = False
        
        if animes:
            for anime in animes:
                link = anime.css("a ::attr(href)").get()
                if link:
                    # yield response.follow(self.scrape_proxy(link), callback=self.parse_detail)
                    yield response.follow(link, callback=self.parse_detail)
                break
    
    def parse_detail(self, response):
        try:
            row_info = response.css('div.spe span')
        except:
            row_info = False
        
        if row_info:
            detail_anime = {}
            for info in row_info:
                try:
                    key = info.css('b::text').get().strip()
                    value = info.css('span::text').get().strip()
                except:
                    key = None
                    value = None
                
                if value is not None:
                    detail_anime[key] = value
            
            if len(detail_anime) != 0:
                self.anime_items['title'] = response.css('div.infox h3::text').get()
                self.anime_items['detail'] = detail_anime
                yield self.anime_items
            
            listeps = response.css('div.listeps ul li')
            for index, eps in enumerate(reversed(listeps)):
                index += 1
                link = eps.css('span a ::attr(href)').get().strip()
                # print(f'link parse detail {link}')
                # yield response.follow(self.scrape_proxy(link), callback=self.parse_download_links, meta={'list_eps': list_eps, 'title': title, 'relesed': relesed})
                if link:
                    # print(f'yield {link} berjalan')
                    yield response.follow(link, callback=self.parse_download_links, meta={'index': index})
                    # yield response.follow(self.scrape_proxy(link), callback=self.parse_download_links, meta={'index': index})
        
        # yield self.anime_items
        # print("-"*5 + f"DONE {self.anime_items['title']}" + "-"*5)
        
    def parse_download_links(self, response):
        # list_eps = response.meta['list_eps']
        # title = response.meta['title']
        # relesed = response.meta['relesed']
        # title = response.css('div.lm h1.entry-title::text').get().strip()
        try:
            title = response.css('div.lm div.entry-content b::text')[-1].get()
        except:
            title = False
            
        if title:
            index = response.meta['index']
            linkdbs = response.css('div.pencenter div.download-eps')
            link_download_mp4 = {}
            link_download_ = {}
            list_eps = {}
            for format_ in linkdbs:
                frmt = format_.css('p ::text').get()
                # print(f'Format Download {frmt}')
                # if 'MP4' in frmt or frmt == 'MP4' or frmt == 'MKV' or 'MKV' in frmt:
                linkdbs_ = format_.css('ul li')
                for linkdb in linkdbs_:
                    dld_link = {}
                    resolusi = linkdb.css('strong::text').get()
                    link_db_resolusi = linkdb.css('span')
                    for dwd in link_db_resolusi:
                        name_download = dwd.css('a ::text').get()
                        link_download = dwd.css('a ::attr(href)').get()
                        dld_link[name_download] = link_download
                    link_download_[resolusi.strip()] = {'link': dld_link}
                    
                link_download_mp4[frmt.strip()] = link_download_
                link_download_ = {}
                
                
                
            lasteps = response.css('div.lstepsiode ul li')
            for eps in lasteps:
                title_eps = eps.css('div.epsright a ::attr(title)').get()
                # print(f'title parse download link eps {title_eps}')
                # print(f"title parse download link {title}")
                if title_eps == title:
                    # print('Eps ditemukan')
                    link_eps = eps.css('div.epsright a ::attr(href)').get()
                    thumbnail = eps.css('div.epsright img ::attr(src)').get()
                    relesed = eps.css('div.epsleft span.date ::text').get()
                    list_eps = {'index': index, 'title': title,'thumbnail': thumbnail, 'relesed': relesed, 'link_sreaming' :link_eps,'link_download': link_download_mp4}
                    break
            
            if len(list_eps) != 0:
                self.anime_eps['episodes'] = list_eps
                yield self.anime_eps