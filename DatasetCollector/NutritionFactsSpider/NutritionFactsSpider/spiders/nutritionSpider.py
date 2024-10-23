
from itemloaders import ItemLoader
import scrapy
import time
import re

from NutritionFactsSpider.items import NutritionItem
from scrapy.loader.processors import MapCompose, TakeFirst


class NutritionSpider(scrapy.Spider):
    name = "nutrition_spider"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    def clean_data(self, data):
        if not data.get('value'):
            data['value'] = '-'
        if not data.get('dv'):
            data['dv'] = '-'
        match = re.search(r'\d+(\.\d+)?', data['value'])
        data['value'] = match.group(0) if match else '-'
        match = re.search(r'\d+(\.\d+)?', data['dv'])
        data['dv'] = match.group(0) if match else '-'
        return data

    def start_requests(self):

        for i in range(173000, 174000):
            time.sleep(0.5)
            url = f"https://tools.myfooddata.com/nutrition-facts/{i}/100g/1"
            # url = "https://ipinfo.io/json"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        if response.status == 200 and response.css("#foodNotFound").get() == None:

            l = ItemLoader(item=NutritionItem(), selector=response)
            # Use TakeFirst to store a single value instead of a list
            l.default_output_processor = TakeFirst()
            # name
            l.add_css("name", ".nutritionFactsTitle::text")

            # calorie
            calorie = {
                'value': response.css(".nft-cal-amt::text").get(),
                'dv': '-'
            }
            if calorie['value'] == '--':
                return
            l.add_value("calorie", calorie, MapCompose(self.clean_data))

            # total_fat
            total_fat = {
                'value': response.css('.FAT::text').get(),
                'dv': response.css('.FATDV::text').get()
            }
            l.add_value("total_fat", total_fat, MapCompose(self.clean_data))

            # saturated_fat
            saturated_fat = {
                'value': response.css('.FASAT::text').get(),
                'dv': response.css('.FASATDV::text').get()
            }
            l.add_value("saturated_fat", saturated_fat, MapCompose(self.clean_data))

            # trans_fat
            trans_fat = {
                'value': response.css('.FATRN::text').get(),
                'dv': '-'
            }
            l.add_value("trans_fat", trans_fat, MapCompose(self.clean_data))

            # cholesterol
            cholesterol = {
                'value': response.css('.CHOLE::text').get(),
                'dv': response.css('.CHOLEDV::text').get()
            }
            l.add_value("cholesterol", cholesterol, MapCompose(self.clean_data))

            # sodium
            sodium = {
                'value': response.css('.NA::text').get(),
                'dv': response.css('.NADV::text').get()
            }
            l.add_value("sodium", sodium, MapCompose(self.clean_data))

            # total_carbohydrate
            total_carbohydrate = {
                'value': response.css('.CHOCDF::text').get(),
                'dv': response.css('.CHOCDFDV::text').get()
            }
            l.add_value("total_carbohydrate", total_carbohydrate, MapCompose(self.clean_data))

            # dietary_fiber
            dietary_fiber = {
                'value': response.css('.FIBTG::text').get(),
                'dv': response.css('.FIBTGDV::text').get()
            }
            l.add_value("dietary_fiber", dietary_fiber, MapCompose(self.clean_data))

            # total_sugars
            total_sugars = {
                'value': response.css('.SUGAR::text').get(),
                'dv': response.css('.SUGARDV::text').get()
            }
            l.add_value("total_sugars", total_sugars, MapCompose(self.clean_data))

            # added_sugars
            added_sugars = {
                'value': response.css('.ADD_SG::text').get(),
                'dv': response.css('.ADD_SGDV::text').get()
            }
            l.add_value("added_sugars", added_sugars, MapCompose(self.clean_data))

            # protein
            protein = {
                'value': response.css('.PROCNT::text').get(),
                'dv': response.css('.PROCNTDV::text').get()
            }
            l.add_value("protein", protein, MapCompose(self.clean_data))

            # vitamin_c
            vitamin_c = {
                'value': response.css('.VITC::text').get(),
                'dv': response.css('.VITCDV::text').get()
            }
            l.add_value("vitamin_c", vitamin_c, MapCompose(self.clean_data))

            # vitamin_d
            vitamin_d = {
                'value': response.css('.VITD::text').get(),
                'dv': response.css('.VITDDV::text').get()
            }
            l.add_value("vitamin_d", vitamin_d, MapCompose(self.clean_data))

            # iron
            iron = {
                'value': response.css('.FE::text').get(),
                'dv': response.css('.FEDV::text').get()
            }
            l.add_value("iron", iron, MapCompose(self.clean_data))

            # calcium
            calcium = {
                'value': response.css('.CA::text').get(),
                'dv': response.css('.CADV::text').get()
            }
            l.add_value("calcium", calcium, MapCompose(self.clean_data))

            # potassium
            potassium = {
                'value': response.css('.K::text').get(),
                'dv': response.css('.KDV::text').get()
            }
            l.add_value("potassium", potassium, MapCompose(self.clean_data))

            # phosphorus
            phosphorus = {
                'value': response.css('.P::text').get(),
                'dv': response.css('.PDV::text').get()
            }
            l.add_value("phosphorus", phosphorus, MapCompose(self.clean_data))

            yield l.load_item()
