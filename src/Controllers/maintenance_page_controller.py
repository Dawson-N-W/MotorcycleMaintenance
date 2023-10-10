from src.Models.DatabaseManager import DatabaseManager
from src.Models.maintenance import Maintenance

db = DatabaseManager()

def find_all_bikes():
    if db.get_all_bikes() == []:
        return -1
    return db.get_all_bikes()

def find_all_maintenance(bikenum):
    if db.get_maintenance(bikenum) == []:
        return -1
    return db.get_maintenance(bikenum)

def add_maintenance(bikenum, oil, oil_filter, transmission_oil, air_filter, spark_plugs, chain, tires, brakes, brake_fluid):
    maintenance = Maintenance(oil, oil_filter, transmission_oil, air_filter, spark_plugs, chain, tires, brakes, brake_fluid)
    if db.get_maintenance(bikenum) != None:
        if db.update_maintenance(bikenum, maintenance) == -1:
            return -1
    else:
        if db.add_maintenance(bikenum, maintenance) == -1:
            return -1
    return 0
def find_bike(bikenum):
    if db.get_bike(bikenum) == None:
        return -1
    return db.get_bike(bikenum)
    