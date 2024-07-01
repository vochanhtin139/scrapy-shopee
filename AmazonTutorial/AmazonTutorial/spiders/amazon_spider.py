import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon_spider"
    allowed_domains = ["shopee.vn"]
    start_urls = [
        "https://shopee.vn/%C4%90i%E1%BB%87n-tho%E1%BA%A1i-Apple-iPhone-15-128GB-i.88201679.18093055535?sp_atk=c9d4c12a-2862-435a-bb85-caf1dfece61c&xptdk=c9d4c12a-2862-435a-bb85-caf1dfece61c"
    ]

    def parse(self, response):
        items = AmazontutorialItem()
        
        # Extract the entire HTML content of the response
        html_content = response.body
        
        items["product_html"] = html_content.decode('utf-8')  # Store as string in the item

        yield items
