# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class ScrapesamehadaSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class ScrapesamehadaDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


import requests
from random import randint
from urllib.parse import urlencode


class ScrapeOpsFakeBrowserHeaderAgentMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def __init__(self, settings):
        self.scrapeops_api_key = settings.get('SCRAPEOPS_API_KEY')
        self.scrapeops_endpoint = settings.get('SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT', 'http://headers.scrapeops.io/v1/browser-headers') 
        self.scrapeops_fake_browser_headers_active = settings.get('SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED', True)
        self.scrapeops_num_results = settings.get('SCRAPEOPS_NUM_RESULTS')
        self.headers_list = []
        self._get_headers_list()
        self._scrapeops_fake_browser_headers_enabled()

    def _get_headers_list(self):
        payload = {'api_key': self.scrapeops_api_key}
        if self.scrapeops_num_results is not None:
            payload['num_results'] = self.scrapeops_num_results
        response = requests.get(self.scrapeops_endpoint, params=urlencode(payload))
        json_response = response.json()
        self.headers_list = json_response.get('result', [])

    def _get_random_browser_header(self):
        random_index = randint(0, len(self.headers_list) - 1)
        return self.headers_list[random_index]

    def _scrapeops_fake_browser_headers_enabled(self):
        if self.scrapeops_api_key is None or self.scrapeops_api_key == '' or self.scrapeops_fake_browser_headers_active == False:
            self.scrapeops_fake_browser_headers_active = False
        else:
            self.scrapeops_fake_browser_headers_active = True
    
    def process_request(self, request, spider):        
        random_browser_header = self._get_random_browser_header()

        request.headers['accept-language'] = random_browser_header['accept-language']
        request.headers['sec-fetch-user'] = random_browser_header['sec-fetch-user'] 
        request.headers['sec-fetch-mod'] = random_browser_header['sec-fetch-mod'] 
        request.headers['sec-fetch-site'] = random_browser_header['sec-fetch-site'] 
        request.headers['sec-ch-ua-platform'] = random_browser_header['sec-ch-ua-platform'] 
        request.headers['sec-ch-ua-mobile'] = random_browser_header['sec-ch-ua-mobile'] 
        request.headers['sec-ch-ua'] = random_browser_header['sec-ch-ua'] 
        request.headers['accept'] = random_browser_header['accept'] 
        request.headers['user-agent'] = random_browser_header['user-agent'] 
        request.headers['upgrade-insecure-requests'] = random_browser_header.get('upgrade-insecure-requests')



class myProxyMiddleware(object):
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)
    
    def __init__(self):
        self.list_proxies = []
        self._get_list_proxy()
    
    
    def _get_list_proxy(self):
        response = requests.get('https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=protocolipport&format=text')
        if response.status_code == 200:
            self.list_proxies = response.text.strip().splitlines()
        else:
            pass
    
    def _get_random_proxies(self):
        random_index = randint(0, len(self.list_proxies) - 1)
        return self.list_proxies[random_index]
    
    def process_request(self, request, spider):
        random_proxies = self._get_random_proxies()




from urllib.parse import urlencode
from scrapy import signals

class RotateAPIKeyMiddleware:
    def __init__(self):
        # Inisialisasi daftar API key
        self.api_keys = [
            '7af7f72914a1a7614cf231699b1d37a3',
            '7376f091c169b76dac672ef1702b26bf',
            '75a9f4992072d7f915923ba99fb69aa0',
            # Tambahkan lebih banyak API key di sini
        ]
        self.current_api_index = 0  # Mulai dengan API key pertama

    def get_current_api_key(self):
        # Mendapatkan API key yang sedang digunakan
        return self.api_keys[self.current_api_index]

    def rotate_api_key(self):
        # Rotasi ke API key berikutnya
        self.current_api_index = (self.current_api_index + 1) % len(self.api_keys)
        print(f"Rotating to next API key: {self.get_current_api_key()}")

    def create_proxy_url(self, url):
        # Membuat URL proxy dengan API key yang sedang aktif
        payload = {'api_key': self.get_current_api_key(), 'url': url}
        proxy_url = 'https://api.scraperapi.com/?' + urlencode(payload)
        return proxy_url

    def process_request(self, request, spider):
        # Set proxy URL dengan API key yang saat ini aktif
        proxy_url = self.create_proxy_url(request.url)
        request.meta['proxy'] = proxy_url
        spider.logger.info(f"Using proxy URL: {proxy_url}")

    def process_response(self, request, response, spider):
        # Memeriksa status respons, jika 403 maka rotasi API key dan ulangi permintaan
        if response.status == 403:
            spider.logger.warning(f"Received 403 error with API key {self.get_current_api_key()}, rotating key...")
            self.rotate_api_key()  # Rotasi ke API key berikutnya
            # Membuat ulang permintaan dengan API key baru
            new_request = request.copy()
            new_request.meta['proxy'] = self.create_proxy_url(request.url)
            return new_request  # Mengirim ulang permintaan dengan API key baru
        return response