from src.Models.DatabaseManager import DatabaseManager
from src.Models.motorcycle_spec import MotorcycleSpecModel


db = DatabaseManager()

def fetch_and_store_motorcycle(make, model, year, mileage):
    if make == '' or model == '' or year == '' or mileage == '':
        return -1
    # Fetch specs from web
    motorcycle = MotorcycleSpecModel(int(year), make, model, int(mileage))
    if motorcycle.success == False:
        return -1
    db.add_motorcycle(motorcycle)
    return 0
    

    
    

