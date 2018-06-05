import scrapy
from slugify import slugify


class OnePageSpider(scrapy.Spider):
    name = "onepage"

    def start_requests(self):
        urls = [
            'https://printmazing.com/products/newfoundland-awesome-luggage-covers-2103?variant=11289208160299'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        index = 0
        handle =  slugify(extract_with_css('title::text').split("-")[0])
        for quote in response.xpath('//div[@class="gallery-cell"]'):
            if index == 1:
                yield {
                    'Handle':handle,
                    'title': extract_with_css('title::text').split("-")[0],
                    'Image Src':quote.xpath('a/@href').extract(),
                    'Image Position':index,    
                    'body': '',
                    'Published': 'TRUE',
                }
            else:
                if (quote.xpath('a/@href').extract_first().strip() != ""):    
                    yield {
                        'Handle':handle,
                        'title': '',
                        'Image Src':quote.xpath('a/@href').extract_first().strip(),
                        'Image Position': index,
                        'body':'',
                        'Published': 'TRUE',
                    }
            index = index + 1          