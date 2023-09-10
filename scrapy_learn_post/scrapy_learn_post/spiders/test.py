import json

import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["fanyi.baidu.com"]

    # post请求不携带参数无法访问
    # start_urls = ["https://fanyi.baidu.com/sug"]

    # def parse(self, response):
    #     pass
    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'
        data = {
            'kw': 'movie'
        }
        yield scrapy.FormRequest(url=url, formdata=data, callback=self.test)

    def test(self, response):
        content = response.text
        obj = json.loads(content)
        print(obj)
