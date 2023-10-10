from src.Models.DatabaseManager import DatabaseManager

db = DatabaseManager()

def find_all_bikes():
    if db.get_all_bikes() == []:
        return -1
    return db.get_all_bikes()

def delete_bike(bikenum):
    if db.delete_bike(bikenum) == -1:
        return -1
    return 0