from src.Models.DatabaseManager import DatabaseManager

db = DatabaseManager()

def find_all_bikes():
    if db.get_all_bikes() == []:
        return -1
    return db.get_all_bikes()

def update_bike_mileage(bike_num, mileage):
    if db.update_mileage(mileage, bike_num) == -1:
        return -1
    return 0