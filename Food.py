from usda.client import UsdaClient
from Vision import Detector
import requests
import json
# Account Email: erictrinn123@gmail.com
# Account ID: 44e1b184-d7b6-412e-9203-495557c36978
client = UsdaClient("my_key") 
foods = client.list_foods(5)


class Food:
    def __init__(self, name = ""):
        self.name = name
        self.raw_data = []
        self.nutrition = dict() #{nutrient_name: (amount, measure_unit)}


    def createRequest(self):
        # https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY&query=Cheddar%20Cheese
        URL = "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=my_key&query="
        full_URL = URL + self.name
        r = requests.get(url = full_URL) #response from API server
        data = r.json() #comes in a json file
        return data

    def getNutrition(self, json_data):
        #list of dictionaries, each nested dictionary contains each specific nutrient {"nutrientId": 1004,"nutrientName": "Total lipid (fat)", "nutrientNumber": "204""unitName": "G","derivationCode": "LCCD","derivationDescription": "Calculated from a daily value percentage per serving size measure","value": 0.0}
        nutrition_data = json_data['foods'][0]['foodNutrients'] 
        self.raw_data = nutrition_data

    def processData(self):
        for nutrtient_dict in self.raw_data:
            nutrient_name = nutrtient_dict['nutrientName'].split(',')[0]
            amount = nutrtient_dict['value']
            measure_unit = nutrtient_dict['unitName']
            self.nutrition[nutrient_name] = (amount, measure_unit)   #1st index of tuple is amount and 2nd index is unit of measure

    def start(self):
        response_json = self.createRequest()
        self.getNutrition(response_json)
        self.processData()



if __name__ == "__main__":
    food_object = Food("cheese")
    food_object.start()

