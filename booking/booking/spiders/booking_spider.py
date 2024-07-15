import scrapy
from booking.items import BookingItem

class BookingSpiderSpider(scrapy.Spider):
    name = "booking_spider"
    allowed_domains = ["www.booking.com"]
    start_urls = ["https://www.booking.com"]

    def parse(self, response):
        cards = response.css('div[data-testid="property-card-container"] > .c655c9a144')

        for card in cards:
            print('\n\n\n')
            item = BookingItem()

            item['name'] = card.css('h3 div[data-testid="title"] ::text').get()
            item['remark'] = card.css('div.d0522b0cca.eb02592978.f374b67e8c ::text').get()
            item['price'] = card.css('span[data-testid="price-and-discounted-price"] ::text').get()
            item['link'] = card.css('div.e8acaa0d22.c4cbd52971 > a').attrib['href']
            item['reviews'] = card.css('div.e8acaa0d22.ab107395cb.c60bada9e4 ::text').get()
            item['ratings'] = card.css('.d0522b0cca.fd44f541d8 > div.a447b19dfd ::text').get()

            yield item
        
