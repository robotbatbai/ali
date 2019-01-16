import scrapy
from slugify import slugify
from pprint import pprint

from . import ali_config
item = ali_config.duvetClass()

class OneSpider(scrapy.Spider):
    name = "one"
    def start_requests(self):
        global item
        urls = item.url
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
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
        #tags_list = item.tags_list #title.replace(" ",",")
        #productType = item.productType
        for image in response.css(item.spiltImage).extract():
            images = edit_image(image)
            if index == 0:
                yield {
                    'Handle':handle,
                    'title': title,
                    'Body (HTML)':item.body,
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