import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon_spider"
    allowed_domains = ["amazon.com"]
    start_urls = [
        # "https://www.amazon.com/s?k=eternal+sunshine&crid=3117XCVNYTC56&sprefix=eternal+sunshi%2Caps%2C340&ref=nb_sb_noss_2"
        "https://shopee.vn/%C4%90i%E1%BB%87n-tho%E1%BA%A1i-Apple-iPhone-15-128GB-i.88201679.18093055535?sp_atk=c9d4c12a-2862-435a-bb85-caf1dfece61c&xptdk=c9d4c12a-2862-435a-bb85-caf1dfece61c"
    ]

    def parse(self, response):
        items = AmazontutorialItem()
        # product_name = response.css('.a-size-medium.a-color-base.a-text-normal::text').extract()
        # product_price = response.css('.a-price-fraction, .a-price-whole').css("::text").extract()
        # product_imagelink = response.css('.s-image-optimized-rendering::attr(src)').extract()
        test = response.css("html").extract()
        
        items["product_name"] = test
        # items["product_price"] = product_price
        # items["product_imagelink"] = product_imagelink
        
        yield items