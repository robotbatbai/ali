import scrapy
from slugify import slugify


class PrintAmazingSpider(scrapy.Spider):
    name = 'printamazing'

    start_urls = ['https://printmazing.com/search?type=product&q=HOODED+BLANKET']

    def parse(self, response):
        def extract_with_xpath(query):
            return response.xpath(query).extract_first().strip()
        domain = 'https://printmazing.com'

        # follow links to author pages
        for product in response.css('div.thumbnail-overlay'):
            product_href = domain + product.xpath('a/@href').extract_first().strip()
            yield response.follow(product_href, self.parse_product)

        # follow pagination links
        for href in response.css('span.next a::attr(href)').extract():
            yield response.follow(domain + href, self.parse)

    def parse_product(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
        def extract_with_xpath(query):
            return response.xpath(query).extract_first().strip()    

        index = 0
        size = ['S','M']
        handle =  slugify(extract_with_css('title::text').split(" - ")[0])
        for quote in response.xpath('//div[@class="gallery-cell"]'):
            images = 'https:' + quote.xpath('a/@href').extract_first().strip()
            #if images is None
             #   continue
            if index == 0:
                yield {
                    'Handle':handle,
                    'title': extract_with_css('title::text').split("-")[0],
                    'Body (HTML)':'',
                    'Vendor':'',
                    'Type':'',
                    'Tags':'',
                    'Published':'TRUE',
                    'Option1 Name':'Size',
                    'Option1 Value':size[index] if len(size) > index else "",
                    'Option2 Name':'',
                    'Option2 Value':'',
                    'Option3 Name':'',
                    'Option3 Value':'',
                    'Variant SKU':'',
                    'Variant Grams':'',
                    'Variant Inventory Tracker':'',
                    'Variant Inventory Qty':'50' if len(size) > index else "",
                    'Variant Inventory Policy':'deny' if len(size) > index else "",
                    'Variant Fulfillment Service':'manual' if len(size) > index else "",
                    'Variant Price': '89' if len(size) > index else "",
                    'Variant Compare At Price':'178' if len(size) > index else "",
                    'Variant Requires Shipping':'',
                    'Variant Taxable':'',
                    'Variant Barcode':'',
                    'Image Src' : images,
                    'Image Position':index +1,   
                    'Image Alt Text':'',
                }
            else:
                if (quote.xpath('a/@href').extract_first().strip() != ""):    
                    yield {
                        'Handle':handle,
                        'title': extract_with_css('title::text').split("-")[0],
                        'Body (HTML)':'',
                        'Vendor':'',
                        'Type':'',
                        'Tags':'',
                        'Published':'TRUE' if len(size) > index else "",
                        'Option1 Name':'',
                        'Option1 Value':size[index] if len(size) > index else "",
                        'Option2 Name':'',
                        'Option2 Value':'',
                        'Option3 Name':'',
                        'Option3 Value':'',
                        'Variant SKU':'',
                        'Variant Grams':'',
                        'Variant Inventory Tracker':'',
                        'Variant Inventory Qty':'50' if len(size) > index else "",
                        'Variant Inventory Policy':'deny' if len(size) > index else "",
                        'Variant Fulfillment Service':'manual' if len(size) > index else "",
                        'Variant Price': '89' if len(size) > index else "",
                        'Variant Compare At Price':'178' if len(size) > index else "",
                        'Variant Requires Shipping':'',
                        'Variant Taxable':'',
                        'Variant Barcode':'',
                        'Image Src' : images,
                        'Image Position':index +1,   
                        'Image Alt Text':'',
                    }
            index += 1      
        while (index < len(size)):
            yield {
                    'Handle':handle,
                    'title': '',
                    'Body (HTML)':'',
                    'Vendor':'',
                    'Type':'',
                    'Tags':'',
                    'Published':'',
                    'Option1 Name':'',
                    'Option1 Value':'',
                    'Option2 Name':'',
                    'Option2 Value':'',
                    'Option3 Name':'',
                    'Option3 Value':'',
                    'Variant SKU':'',
                    'Variant Grams':'',
                    'Variant Inventory Tracker':'',
                    'Variant Inventory Qty':'',
                    'Variant Inventory Policy':'',
                    'Variant Fulfillment Service':'',
                    'Variant Price': '',
                    'Variant Compare At Price':'',
                    'Variant Requires Shipping':'',
                    'Variant Taxable':'',
                    'Variant Barcode':'',
                    'Image Src' : images,
                    'Image Position':index +1,   
                    'Image Alt Text':'',
            }
            index +=  1  