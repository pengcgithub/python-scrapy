# -*- coding: utf-8 -*-
import scrapy
from scrapyspider.items import ScrapyspiderItem


class YfSpider(scrapy.Spider):
    name = 'yf'
    allowed_domains = ['yingfeng365.com']
    start_urls = ['http://www.yingfeng365.com/news/frontinfo?page=1']
    # scrapy crawl yf

    def parse(self, response):
        info_list = response.xpath('//ul/li[@class="info_list"]')
        for info in info_list:
            image = info.xpath('./a/img[1]/@src').get()
            title = info.xpath("./a/div/h3[@class='info-list-title']/text()").get()
            time = info.xpath("./a/div/p[@class='info-list-time']/text()").get()
            result = ScrapyspiderItem(title=title, time=time, image=image)
            yield result
