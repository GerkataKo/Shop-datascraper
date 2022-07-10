import scrapy
from scrapy_selenium import SeleniumRequest


class ScrapySeleniumSpider(scrapy.Spider):
    name = 'scrapy-selenium'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99',
            wait_time=3,
            screenshot=True,
            callback=self.parse,
            dont_filter=True

        )

    custom_settings = {'FEED_URI': "mango-shop.json",
                       'FEED_FORMAT': 'json'}

    def parse(self, response):
        name = response.xpath('//*[@id="app"]/main/div/div[3]/div[1]/div[1]/h1/text()').get()
        price = float(response.xpath('//*[@id="app"]/main/div/div[3]/div[1]/div[2]/span[2]/text()').get().split(".", 1)[1])
        discounted_price = float(response.xpath('//*[@id="app"]/main/div/div[3]/div[1]/div[2]/span[4]/text()').get().split(".", 1)[1])
        colour = response.xpath('//*[@id="app"]/main/div/div[3]/div[2]/div[2]/span/text()').get()
        sizes = response.css('span.size-unavailable::text').getall()


        yield {
            'Name': name,
            'Price': price,
            'Discounted_price': discounted_price,
            'Colour': colour,
            'Sizes': sizes
        }
