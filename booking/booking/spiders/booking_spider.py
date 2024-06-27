import scrapy
from booking.items import BookingItem

class BookingSpiderSpider(scrapy.Spider):
    name = "booking_spider"
    allowed_domains = ["www.booking.com"]
    start_urls = ["https://www.booking.com"]

    def parse(self, response):

        cards = response.css('div[data-testid="property-card-container"]')

        for card in cards:
            booking = BookingItem()

            
            booking['name'] =  card.css('div[data-testid="title"]::text').get()
            booking['remark'] = card.css('div.f13857cc8c.e6314e676b.a287ba9834::text').get()
            booking['score'] = card.css('div.f13857cc8c.e008572b71::text').get()
            if card.css('div.b290e5dfa6.a5cc9f664c.c4b07b6aa8::text').get() is not None:
                booking['review'] = card.css('div.b290e5dfa6.a5cc9f664c.c4b07b6aa8::text').get().split(" ")[0]
            else:
                booking['review'] = "0"
            booking['location'] = card.css('div.b290e5dfa6.bca66f8f42 a::attr(href)') .get()
            booking['price'] = card.css('span.fa4a3a8221.b22052b420.f53c51ec80 ::text').get()

            yield booking
        
