# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
import json
import pandas as pd

class CleanDataPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        text = adapter.get('text')
        if text:
            adapter['text'] = text.strip()

        return item
    
class JsonWriterPipeline:
    def open_spider(self, spider):
        self.file=open('films.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    
    def close_spider(self, spider):
        self.file.close()

class ExcelWriterPipeline:
    def open_spider(self, spider):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item

    def close_spider(self, spider):
        df = pd.DataFrame(self.items)
        df.to_excel("films.xlsx", index=False)