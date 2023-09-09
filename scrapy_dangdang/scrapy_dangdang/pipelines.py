# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyDangdangPipeline:
    def open_spider(self,spider):
        self.fp = open('book.json', 'a', encoding='utf-8')

    # item就是yield返回的对象
    def process_item(self, item, spider):
        # with open('book.json', 'a', encoding='utf-8') as fp:
        #     fp.write(str(item))
        self.fp.write(str(item))
        return item

    def close_spider(self, spider):
        self.fp.close()