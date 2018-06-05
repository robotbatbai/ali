import scrapy
from slugify import slugify


class OnePageSpider(scrapy.Spider):
    name = "onepage"

    def start_requests(self):
        urls = [
            'https://www.shopyplace.com/products/large-capacity-hanging-travel-organizer'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        index = 0
        for quote in response.xpath('//li[@data-thumb]'):
            if index == 0:
                yield {
                    'image':quote.xpath('a/@href').extract(),
                    'title': slugify(extract_with_css('title::text').split("-")[0]),
                }
                index = index + 1 
            else:    
                yield {
                    'image':quote.xpath('a/@href').extract(),
                    'title':' ',
                }     