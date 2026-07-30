import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ["https://webscraper.io/test-sites/e-commerce/allinone"]

    def parse(self, response):
        products = response.css(".thumbnail")
        for product in products:
            yield {
                "title": product.css("a.title::attr(title)").get(),
                "price": product.css(".price::text").get(),
                "description": product.css(".description::text").get(),
            }