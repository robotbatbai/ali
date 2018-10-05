import scrapy


class ShopyPlaceSpider(scrapy.Spider):
    name = 'shopyplace'

    start_urls = ['https://www.shopyplace.com/collections/all']

    def parse(self, response):
        # follow links to author pages
        for href in response.css('a[itemprop="url"]::attr(href)'):
            yield response.follow(href, self.parse_author)

        # follow pagination links
        for href in response.css('span.next a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'title': extract_with_css('title::text'),
        }