import scrapy
from slugify import slugify
from pprint import pprint
from random import randint

from . import ali_config
item = ali_config.duvetClass()

class ListSpider(scrapy.Spider):
    name = 'list'
    global item

    start_urls = item.urls 
    def parse(self, response):
        global item
        def extract_with_xpath(query):
            return response.xpath(query).extract_first().strip()
        domain = 'https:'

        # follow links to author pages
        for product in response.css(item.pageDetail):
            product_href = domain + product.xpath('a/@href').extract_first().strip()
            yield response.follow(product_href, self.parse_product)

        # follow pagination links
        for href in response.css(item.nextPage).extract():
            yield response.follow(domain + href, self.parse)

    def parse_product(self, response):
        global item
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
        def extract_with_xpath(query):
            return response.xpath(query).extract_first().strip()   
        def edit_image(image):
            return image.rsplit("_",1)[0]
        def remove_trademark(title):  
            global item
            for ch in item.replaceList:
                if ch in title: 
                    title = title.replace(ch,"")
            return ' '.join(title.split())
     
        title = remove_trademark(extract_with_css(item.title))
        print(title)
        handle =  slugify(title)
        size = item.size
        index = 0
        body = item.body[randint(0,3)]
        #tags_list = item.tags_list #title.replace(" ",",")
        #productType = item.productType
        for image in response.css(item.spiltImage).extract():
            images = edit_image(image)
            if index == 0:
                yield {
                    'Handle':handle,
                    'title': title,
                    'Body (HTML)':body,
                    'Vendor':'',
                    'Type': item.productType,
                    'Tags':item.taglist,
                    'Published':'TRUE',
                    'Option1 Name':'Size',
                    'Option1 Value':size[index][0] if len(size) > index else "",
                    'Option2 Name':'',
                    'Option2 Value':'',
                    'Option3 Name':'',
                    'Option3 Value':'',
                    'Variant SKU':'',
                    'Variant Grams':'',
                    'Variant Inventory Tracker':'',
                    'Variant Inventory Qty':50 if len(size) > index else "",
                    'Variant Inventory Policy':'deny' if len(size) > index else "",
                    'Variant Fulfillment Service':'manual' if len(size) > index else "",
                    'Variant Price': size[index][1] if len(size) > index else "",
                    'Variant Compare At Price':size[index][2] if len(size) > index else "",
                    'Variant Requires Shipping':'',
                    'Variant Taxable':'',
                    'Variant Barcode':'',
                    'Image Src' : images,
                    'Image Position':index +1,   
                    'Image Alt Text':'',
                }
            else:
                if (image != ""):    
                    yield {
                        'Handle':handle,
                        'title': '',
                        'Body (HTML)':'',
                        'Vendor':'',
                        'Type':'',
                        'Tags':'',
                        'Published':'TRUE' if len(size) > index else "",
                        'Option1 Name':'',
                        'Option1 Value':size[index][0] if len(size) > index else "",
                        'Option2 Name':'',
                        'Option2 Value':'',
                        'Option3 Name':'',
                        'Option3 Value':'',
                        'Variant SKU':'',
                        'Variant Grams':'',
                        'Variant Inventory Tracker':'',
                        'Variant Inventory Qty':50 if len(size) > index else "",
                        'Variant Inventory Policy':'deny' if len(size) > index else "",
                        'Variant Fulfillment Service':'manual' if len(size) > index else "",
                        'Variant Price': size[index][1] if len(size) > index else "",
                        'Variant Compare At Price':size[index][2] if len(size) > index else "",
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
                    'Published':'TRUE',
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
                    'Variant Price': size[index][1] ,
                    'Variant Compare At Price':size[index][2],
                    'Variant Requires Shipping':'',
                    'Variant Taxable':'',
                    'Variant Barcode':'',
                    'Image Src' : '',
                    'Image Position':'',   
                    'Image Alt Text':'',
            }
            index +=  1   