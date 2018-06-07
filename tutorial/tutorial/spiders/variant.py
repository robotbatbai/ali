import scrapy
from slugify import slugify


class VariantSpider(scrapy.Spider):
    name = "variant"

    def start_requests(self):
        urls = [
            'https://printmazing.com/products/american-pit-bull-terrier-face-all-over-print-full-zip-hoodie-for-men-model-h14'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
        def extract_with_xpath(query):
            return response.xpath(query).extract_first().strip()    

        index = 0
        size = ['S','M','L','XL','XXL','XXXL']
        handle =  slugify(extract_with_css('title::text').split("-")[0])
        for quote in response.xpath('//div[@class="gallery-cell"]'):
            if index == 0:
                yield {
                    'Handle':handle,
                    'title': extract_with_css('title::text').split("-")[0],
                    'Image Src':quote.xpath('a/@href').extract(),
                    'Image Position':index +1,    
                    'body': '',
                    'Published': 'TRUE',
                    'Option1 Name':'Size',
                    'Option1 Value':size[index],
                    'Variant Inventory Qty':'50',
                    #'Variant Price':extract_with_xpath('//span[@class="current_price "]/span[@class="money"]/text()[last()]'),
                }
            else:
                if (quote.xpath('a/@href').extract_first().strip() != ""):    
                    yield {
                        'Handle':handle,
                        'title': '',
                        'Image Src':quote.xpath('a/@href').extract_first().strip(),
                        'Image Position': index + 1,
                        'body':'',
                        'Published': 'TRUE',
                        'Option1 Name':'',
                        'Option1 Value':size[index],
                        'Variant Inventory Qty':'50',
                        #'Variant Price':extract_with_xpath('//span[@itemprop="price"]/following::span[1]/span[@class="money"]/text()[last()]'),
                    }
            index += 1      
    while (index < len(size)):
        yield {
            'Handle':handle,
            'title': '',
            'Image Src':"",
            'Image Position': "",
            'body':'',
            'Published': 'TRUE',
            'Option1 Name':'',
            'Option1 Value':size[index],
            'Variant Inventory Qty':'50',
            #'Variant Price':extract_with_xpath('//span[@itemprop="price"]/following::span[1]/span[@class="money"]/text()[last()]'),
        }
        index +=  1        
                       