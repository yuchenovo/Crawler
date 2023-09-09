import scrapy
from scrapy_dangdang.items import ScrapyDangdangItem


class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.01.00.00.00.00.html"]
    base_url = 'http://category.dangdang.com/pg'
    base_url_end = '-cp01.01.00.00.00.00.html'
    page = 1

    def parse(self, response):
        print('================')
        res_list = response.xpath('//ul[@id="component_59"]/li')
        for res in res_list:
            src = res.xpath('.//img/@data-original').extract_first()
            if src:
                src = src
            else:
                src = res.xpath('.//img/@src').extract_first()
            name = res.xpath('.//img/@alt').extract_first()
            price = res.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            book = ScrapyDangdangItem(src=src, name=name, price=price)
            # 获取对象返回给管道进行下载
            yield book

        if self.page < 100:
            self.page += 1
            url = self.base_url + str(self.page) + self.base_url_end
            yield scrapy.Request(url=url,callback=self.parse)
