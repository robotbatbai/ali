import scrapy
from urllib.parse import unquote
from urllib import request
from slugify import slugify
import json 
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class DemoSpider(scrapy.Spider):
    name = 'demo'

    start_urls = ['https://vio-store.com/collections/all-over-print-shirts']

    def parse(self, response):
        def extract_with_xpath(query):
            return response.xpath(query).extract_first().strip()
        def getPrice(price):
            temp = 1.0 * int(price) / 100
            return temp
        domain = "https://vio-store.com"
        def removeId(image):
            try:
                temp = image.split("?")
                return temp[0]
            except: 
                return ""

        # follow links to author pages
        for product in response.xpath('//a[@class="grid__image"]/@href').extract():
            product_href = domain + product+ ".js"

            with request.urlopen(product_href) as url:
                data = json.loads(url.read().decode())
            
            title = data['title']
            handle = data['handle']
            description = data['description']
            images = data['images']
            options = data['options']
            tags = ','.join(data['tags'])
            variants = data['variants']
            vendor = "print amazing"
            
            i = 0
            for item in variants:
                if i < len(images):
                    image = "https:"+ removeId(images[i])
                    image_option = i + 1
                else:
                    image = ""
                    image_option = ""
                alttext = title + " " + item["option1"]

                try: 
                    variant_image = removeId(item["featured_image"]["src"])
                except:
                    variant_image  = ""

                yield{
                    'Handle': handle,
                    'title': title if i == 0 else "",
                    'Body (HTML)': description if i == 0 else "",
                    'Vendor': vendor,
                    'Type': data["type"] if i == 0 else "",
                    'Tags': tags if i == 0 else "",
                    'Published':'TRUE' if i == 0 else "",
                    'Option1 Name': options[0]["name"] if i == 0 else "",
                    'Option1 Value': item["option1"] ,
                    'Option2 Name': options[1]["name"] if i == 0 else "",
                    'Option2 Value': item["option2"],
                    'Option3 Name':'',
                    'Option3 Value':'',
                    'Variant SKU':'',
                    'Variant Grams':'',
                    'Variant Inventory Tracker':'',
                    'Variant Inventory Qty':50,
                    'Variant Inventory Policy':'deny',
                    'Variant Fulfillment Service':'manual',
                    'Variant Price': getPrice(item["price"]) ,
                    'Variant Compare At Price': getPrice(item["compare_at_price"]),
                    'Variant Requires Shipping':'',
                    'Variant Taxable':'',
                    'Variant Barcode':'',
                    'Image Src' : image,
                    'Image Position':image_option,   
                    'Image Alt Text': alttext if i == 0 else "",
                    'Variant Image':variant_image,
                }
                i += 1

        # follow pagination links
        for href in response.css('span.next a::attr(href)').extract():
            yield response.follow(domain + href, self.parse)
    

        

        


    # def parse_product(self, response):
    #     def extract_with_css(query):
    #         return response.css(query).extract_first().strip()
    #     def extract_with_xpath(query):
    #         return response.xpath(query).extract_first().strip()    



    #     title = remove_trademark(extract_with_css(item.title))
    #     print(title)
    #     handle =  slugify(title)
    #     size = item.size
    #     index = 0
    #     body = item.body[randint(0,3)]
    #     #tags_list = item.tags_list #title.replace(" ",",")
    #     #productType = item.productType
    #     for image in response.css(item.spiltImage).extract():
    #         images = edit_image(image)
    #         if index == 0:
    #             yield {
    #                 'Handle':handle,
    #                 'title': title,
    #                 'Body (HTML)':body,
    #                 'Vendor':'',
    #                 'Type': item.productType,
    #                 'Tags':item.taglist,
    #                 'Published':'TRUE',
    #                 'Option1 Name':'Size',
    #                 'Option1 Value':size[index][0] if len(size) > index else "",
    #                 'Option2 Name':'',
    #                 'Option2 Value':'',
    #                 'Option3 Name':'',
    #                 'Option3 Value':'',
    #                 'Variant SKU':'',
    #                 'Variant Grams':'',
    #                 'Variant Inventory Tracker':'',
    #                 'Variant Inventory Qty':50 if len(size) > index else "",
    #                 'Variant Inventory Policy':'deny' if len(size) > index else "",
    #                 'Variant Fulfillment Service':'manual' if len(size) > index else "",
    #                 'Variant Price': size[index][1] if len(size) > index else "",
    #                 'Variant Compare At Price':size[index][2] if len(size) > index else "",
    #                 'Variant Requires Shipping':'',
    #                 'Variant Taxable':'',
    #                 'Variant Barcode':'',
    #                 'Image Src' : images,
    #                 'Image Position':index +1,   
    #                 'Image Alt Text':'',
    #             }
    #         else:
    #             if (image != ""):    
    #                 yield {
    #                     'Handle':handle,
    #                     'title': '',
    #                     'Body (HTML)':'',
    #                     'Vendor':'',
    #                     'Type':'',
    #                     'Tags':'',
    #                     'Published':'TRUE' if len(size) > index else "",
    #                     'Option1 Name':'',
    #                     'Option1 Value':size[index][0] if len(size) > index else "",
    #                     'Option2 Name':'',
    #                     'Option2 Value':'',
    #                     'Option3 Name':'',
    #                     'Option3 Value':'',
    #                     'Variant SKU':'',
    #                     'Variant Grams':'',
    #                     'Variant Inventory Tracker':'',
    #                     'Variant Inventory Qty':50 if len(size) > index else "",
    #                     'Variant Inventory Policy':'deny' if len(size) > index else "",
    #                     'Variant Fulfillment Service':'manual' if len(size) > index else "",
    #                     'Variant Price': size[index][1] if len(size) > index else "",
    #                     'Variant Compare At Price':size[index][2] if len(size) > index else "",
    #                     'Variant Requires Shipping':'',
    #                     'Variant Taxable':'',
    #                     'Variant Barcode':'',
    #                     'Image Src' : images,
    #                     'Image Position':index +1,   
    #                     'Image Alt Text':'',
    #                 }     
    #         index += 1      
    #     while (index < len(size)):
    #         yield {
    #                 'Handle':handle,
    #                 'title': '',
    #                 'Body (HTML)':'',
    #                 'Vendor':'',
    #                 'Type':'',
    #                 'Tags':'',
    #                 'Published':'TRUE',
    #                 'Option1 Name':'',
    #                 'Option1 Value':size[index],
    #                 'Option2 Name':'',
    #                 'Option2 Value':'',
    #                 'Option3 Name':'',
    #                 'Option3 Value':'',
    #                 'Variant SKU':'',
    #                 'Variant Grams':'',
    #                 'Variant Inventory Tracker':'',
    #                 'Variant Inventory Qty':'50',
    #                 'Variant Inventory Policy':'deny',
    #                 'Variant Fulfillment Service':'manual',
    #                 'Variant Price': size[index][1] ,
    #                 'Variant Compare At Price':size[index][2],
    #                 'Variant Requires Shipping':'',
    #                 'Variant Taxable':'',
    #                 'Variant Barcode':'',
    #                 'Image Src' : '',
    #                 'Image Position':'',   
    #                 'Image Alt Text':'',
    #         }
    #         index +=  1    