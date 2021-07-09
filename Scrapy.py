import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'QuotesSpider'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self,response):
        quotes = response.xpath('*//div[@class="quote"]')
        for q in quotes: #para Q em quotes
            yield {
                'title': q.xpath('.//span[@class="text"]/text()') . get()
                'author': q.xpath('.//small[@class="author"]/text()') .get()
                'tags': q.xpath('.//div[@class="tags"]/a[@class="tag"]/text()') .get()
            }

    proxima_pagina = response.xpath('*//li[@class="next"]/a/@class="next"]/a/@href').get()
    
    if proxima_pagina is not None:
        yield scrapy.Request (response.urljoin(next_pag), callback=self.parse)
        


    