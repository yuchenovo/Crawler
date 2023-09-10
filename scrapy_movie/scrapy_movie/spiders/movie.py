import scrapy

from scrapy_movie.items import ScrapyMovieItem


class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["www.dygod.net"]
    start_urls = ["https://www.dygod.net/html/gndy/china/index.html"]
    src = ''

    def parse(self, response):
        print('=====================================================')
        table_list = response.xpath('//div[@class="co_content8"]//table')
        for table in table_list:
            name = table.xpath('.//a[2]/@title').extract_first()
            url = 'https://www.dygod.net/' + table.xpath('.//a[2]/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_img, meta={'name': name})

    def parse_img(self, response):
        src = 'https://www.dygod.net/' + response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        name = response.meta['name']
        movie = ScrapyMovieItem(name=name, src=src)
        yield movie
