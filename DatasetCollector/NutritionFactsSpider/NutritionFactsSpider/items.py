# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NutritionItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    calorie = scrapy.Field()
    total_fat = scrapy.Field()
    saturated_fat = scrapy.Field()
    trans_fat = scrapy.Field()
    cholesterol = scrapy.Field()
    sodium = scrapy.Field()
    total_carbohydrate = scrapy.Field()
    dietary_fiber = scrapy.Field()
    total_sugars = scrapy.Field()
    added_sugars = scrapy.Field()

    protein = scrapy.Field()
    vitamin_c = scrapy.Field()
    vitamin_d = scrapy.Field()

    iron = scrapy.Field()
    calcium = scrapy.Field()
    potassium = scrapy.Field()
    phosphorus = scrapy.Field()
