# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookingPipeline:
    def process_item(self, item, spider):
        
        adaptor = ItemAdapter(item)

        fields = adaptor.field_names()

        for field in fields:
            if field == "price":
                value = adaptor.get(field)
                adaptor[field] = value.replace(r"\xa", " ")
            if field == "ratings":
                value = adaptor.get(field)
                if value:
                    adaptor[field] = value.split(' ')[1]
                else:
                    adaptor[field] = 0

            if field == "reviews":
                value = adaptor.get(field)
                if value:
                    adaptor[field] = value.split(' ')[0]
                else:
                    adaptor[field] = 0

        return item


