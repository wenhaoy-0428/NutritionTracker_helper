# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import os


class OutputJsonPipeline:
    def __init__(self):
        self.file_name = 'output.json'
        # Create a new file if it doesn't exist
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as f:
                f.write('[\n')  # Start the JSON array

    def process_item(self, item, spider):
        # Convert the item to a JSON string
        line = json.dumps(dict(item)) + ",\n"
        with open(self.file_name, 'a') as f:  # Open in append mode
            f.write(line)
        return item

    def close_spider(self, spider):
        # Close the JSON array when spider is done
        with open(self.file_name, 'a') as f:
            f.write(']\n')  # Close the JSON array
