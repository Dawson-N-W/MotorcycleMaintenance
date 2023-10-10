import requests
import json
import re
import os


class MotorcycleSpecModel:
    make = ''
    model = ''
    year = 0
    engine_type = ''
    engine_size = 0
    horsepower = 0
    torque = 0
    bike_num = 0
    mileage = 0

    success = True
    
    def __init__(self, year, make, model, mileage):
        self.year = year
        self.make = make
        self.model = model
        self.mileage = mileage
        self.get_spec()
    
    def get_spec(self):
        try:
            key = os.environ.get('MOTORCYCLE_API_KEY')
            url = 'https://api.api-ninjas.com/v1/motorcycles?make=' + self.make + '&model=' + self.model + '&year=' + str(self.year)
            response = requests.get(url, headers={'X-Api-Key': key if key else ""})
            json_data = json.loads(response.text)[0]
            self.engine_type = json_data['engine']
            if self.engine_type != 'Electric': self.engine_type = 'Gas'
            cc = re.search(r'(\d+)', json_data['displacement'])
            if cc:
                self.engine_size = int((cc.group(1)))
            hp = re.search(r'(\d+)', json_data['power'])
            if hp:
                self.horsepower = int((hp.group(1)))
            torque = re.search(r'(\d+)', json_data['torque'])
            if torque:
                self.torque = int((torque.group(1)))
            
        except:
            print('Error getting motorcycle spec')
            self.success = False
    
    def set_bike_num(self, bike_num):
        self.bike_num = bike_num

