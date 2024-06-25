import scrapy


class BookingSpiderSpider(scrapy.Spider):
    name = "booking_spider"
    allowed_domains = ["www.booking.com"]
    start_urls = ["https://www.booking.com"]

    def parse(self, response):
        pass
