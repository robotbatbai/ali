import scrapy
from slugify import slugify
from pprint import pprint


class OnePageSpider(scrapy.Spider):
    name = "3page"

    def start_requests(self):
        urls = [
            'https://threelemonshome.com/products/3d-customize-toucan-bedding-set-duvet-cover-set-bedroom-set-bedlinen-8'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
        def extract_with_xpath(query):
            return response.xpath(query).extract_first().strip()    

        index = 0
        body = """<h3><strong>Description:</strong></h3>
            <p>1)This Item&nbsp;Is Customize Style,The Producing Time Is 7-10 Days.</p>
            <p>2)100% Microfiber,Soft and Comfortable.</p>
            <p>3)Environmental Dyeing,Never Lose Color.</p>
            <p>4)2017 Newest Design,German Shepherd,Fashion and Personality.</p>
            <p>5)3pcs Total Have 1pc Duvet Cover/2pcs Pillowcases(Twin Size 1pc),Not Have Any Quilt/Comforter/Filling.</p>
            <p>6)Free Shipping By DHL,Fedex,UPS Express,Safe and Fast.Pls Don't Forget Give Us Your Phone No.</p>
            <div></div>
            <h3><strong>Before You Take Order,Pls Check The Size Chart Below:</strong></h3>
            <p>Twin Size(2 pcs)</p>
            <p>1 pc duvet cover:172*218cm(68*86inch)<br>1 pc pillowcase:50*75cm(19*29inch)<br><br>Full Size(3 pcs)<br>1 pc duvet cover:200*229cm(79*90inch)<br>2 pcs pillowcase:50*75cm(19*29inch)<br><br>Queen Size(3 pcs)<br>1 pc duvet cover:228*228cm(90*90inch)<br>2 pcs pillowcase:50*75cm(19*29inch)<br><br>King Size(3 pcs)<br>1 pc duvet cover:259*229cm(102*90inch)<br>2 pcs pillowcase:50*75cm(19*29inch)</p>
            <p><span>California King Size(3 pcs)</span><br><span>1 pc duvet cover:264*239cm(104*94inch)</span><br><span>2 pcs pillowcase:50*75cm(19*29inch)</span></p>
            <h3>
            <br>Specification:</h3>
            <p><br>1)100% Microfiber Polyester,soft,comfortable and durable.<br>2)Reactive Dying,Non-Fading,Non-Pilling, Non-Wrinkle.<br>3)Fabric Density:130x70,Fabric Count:50x50<br>4)Best choice for your unique bedroom</p>
            <h3>
            <br><br><span>Care:</span>
            </h3>
            <p><br><span>Machine Wash in Cold, Dry on Low.</span></p> """
        size = ['Twin','Full','Queen','King','California King']
        handle =  slugify(extract_with_css('title::text').split(" | ")[0])
        tags = response.css('li.tags a::text').extract()
        tags_list = ''.join(str(e).strip() for e in tags)
        #print(''.join(str(e).strip() for e in tags))
        for quote in response.css('div#gallery_main a.image-thumb::attr(href)').extract():
            images = "https:"+ quote
            if index == 0:
                yield {
                    'Handle':handle,
                    'title': extract_with_css('title::text').split(" | ")[0],
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
                    'Image Alt Text':'',
                }
            else:
                if (quote != ""):    
                    yield {
                        'Handle':handle,
                        'title': extract_with_css('title::text').split(" | ")[0],
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
                    'Option1 Value':size[index] if len(size) > index else "",
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
                    'Image Src' : '',
                    'Image Position':'',   
                    'Image Alt Text':'',
            }
            index +=  1          