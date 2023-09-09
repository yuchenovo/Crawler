import scrapy


class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.01.02.00.00.00"]

    def parse(self, response):
        print('================')
        src = response.xpath('//ul[@id="component_59"]//img/@data-original')
        print(src)
        # res_list = response.xpath('//ul[@id="component_59"]')
        # for res in res_list:
        #
        #     name = res.xpath('.//img/@alt')
        #     price = res.xpath('.//p[@class="price"]/span[1]/text()')
        #     print(src,name,price)
