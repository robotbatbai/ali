import scrapy
from slugify import slugify
from pprint import pprint
from random import randint


class ThreeLemonSpider(scrapy.Spider):
    name = 'threelemon'

    start_urls = ['https://threelemonshome.com/collections/duvet-cover-set']

    def parse(self, response):
        def extract_with_xpath(query):
            return response.xpath(query).extract_first().strip()
        domain = 'https://threelemonshome.com'

        # follow links to author pages
        for product in response.css(' #sandBox div.product-images'):
            product_href = domain + product.xpath('a/@href').extract_first().strip()
            yield response.follow(product_href, self.parse_product)

        # follow pagination links
        for href in response.css('li.next a::attr(href)').extract():
            yield response.follow(domain + href, self.parse)

    def parse_product(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
        def extract_with_xpath(query):
            return response.xpath(query).extract_first().strip()    

        index = 0
        body = ""
        size = ['Twin','Full','Queen','King','California King']

        # bo qua neu co nhieu color 
        colors = response.xpath('//div[@class="variants-wrapper clearfix"]/select/option').extract()
        if (len(colors) > 5):
            return
        # get title tu the h1     
        title = response.xpath('//h1[@class="hidden-phone"]/text()').extract()[0].strip()
        handle =  slugify(title + str(randint(0, 9)))

        #tao link tags 
        tags = response.css('li.tags a::text').extract()
        tags_list = ''.join(str(e).strip() for e in tags)
        for quote in response.css('div#gallery_main a.image-thumb::attr(href)').extract():
            images = "https:"+ quote
            if index == 0:
                yield {
                    'Handle':handle,
                    'title': title,
                    'Body (HTML)':body,
                    'Vendor':'',
                    'Type': extract_with_css('li.type a::text'),
                    'Tags':tags_list,
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
                    'Image Alt Text':title,
                }
            else:
                if (quote != ""):    
                    yield {
                        'Handle':handle,
                        'title': '',
                        'Body (HTML)':'',
                        'Vendor':'',
                        'Type':'',
                        'Tags':'',
                        'Published':"",
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
                        'Image Alt Text':title+tags_list,
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
                    'Option1 Value':size[index],
                    'Option2 Name':'',
                    'Option2 Value':'',
                    'Option3 Name':'',
                    'Option3 Value':'',
                    'Variant SKU':'',
                    'Variant Grams':'',
                    'Variant Inventory Tracker':'',
                    'Variant Inventory Qty':'50',
                    'Variant Inventory Policy':'deny',
                    'Variant Fulfillment Service':'manual',
                    'Variant Price': '89',
                    'Variant Compare At Price':'178',
                    'Variant Requires Shipping':'',
                    'Variant Taxable':'',
                    'Variant Barcode':'',
                    'Image Src' : '',
                    'Image Position':'',   
                    'Image Alt Text':'',
            }
            index +=  1     