import pymysql.cursors
from src.Models.motorcycle_spec import MotorcycleSpecModel
from src.Models.maintenance import Maintenance
import os

class DatabaseManager:
    host = 'localhost'
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASS')
    database = 'Motorcycles'
    
    
    def __init__(self):
        self.connection = self._connect()

    def _connect(self):
        try:
            connection = pymysql.connect(host=self.host,
                                    user=self.user,
                                    password=self.password if self.password else '',
                                    database=self.database,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
            return connection
        except:
            print('Error connecting to database')
            raise Exception('Error connecting to database')
            
        
    def disconnect(self):
        try:
            self.connection.close()
        except:
            print('Error disconnecting from database')
    
    def add_motorcycle(self, MotorcycleSpecModel):

        make = MotorcycleSpecModel.make
        model = MotorcycleSpecModel.model
        year = MotorcycleSpecModel.year
        engine = MotorcycleSpecModel.engine_type
        engine_size = MotorcycleSpecModel.engine_size
        horsepower = MotorcycleSpecModel.horsepower
        torque = MotorcycleSpecModel.torque
        mileage = MotorcycleSpecModel.mileage

        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    sql = "INSERT INTO `Motorcycle` (`Make`, `Model`, `Year`, `EngineType`, `CC`, `Horsepower`, `Torque`, `Mileage`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    self.connection.ping(reconnect=True)
                    cursor.execute(sql, (make, model, year, engine, engine_size, horsepower, torque, mileage))
                    self.connection.commit()
                    MotorcycleSpecModel.set_bike_num(self._get_bike_num(make, model, year))
                   
        except Exception as e:
            print(str(e))
        
    
    def _get_bike_num(self, make, model, year):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT `BikeNum` FROM `Motorcycle` WHERE `Make` = %s AND `Model` = %s AND `Year` = %s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (make, model, year))
                result = cursor.fetchone()
                return result['BikeNum'] if result else None
        except Exception as e:
            print(str(e))


    def get_mileage(self, bike_num):
        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    sql = "SELECT `Motorcycle` FROM `Mileage` WHERE `BikeNum` = %s"
                    self.connection.ping(reconnect=True)
                    cursor.execute(sql, (bike_num))
                    result = cursor.fetchone()
                    return result['Mileage'] if result else None
        except:
            print('Error getting mileage from database')
    
    def update_mileage(self, mileage, bike_num):
        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    sql = "UPDATE `Motorcycle` SET `Mileage` = %s WHERE `BikeNum` = %s"
                    self.connection.ping(reconnect=True)
                    cursor.execute(sql, (mileage, bike_num))
                    self.connection.commit()
        except:
            print('Error updating mileage in database')
    

    def delete_bike(self, bike_num):
        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    sql = "DELETE FROM `Motorcycle` WHERE `BikeNum` = %s"
                    self.connection.ping(reconnect=True)
                    cursor.execute(sql, (bike_num))
                    self.connection.commit()
        except:
            print('Error deleting bike from database')
    
    def get_bike(self, bike_num):
        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    sql = "SELECT * FROM `Motorcycle` WHERE `BikeNum` = %s"
                    self.connection.ping(reconnect=True)
                    cursor.execute(sql, (bike_num))
                    result = cursor.fetchone()
                    return result if result else None
        except:
            print('Error getting bike from database')
    
    def get_all_bikes(self):
        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    sql = "SELECT * FROM `Motorcycle`"
                    self.connection.ping(reconnect=True)
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    return result
        except:
            print('Error getting all bikes from database')
    
    def add_maintenance(self, bike_num, Maintenance):
        oil = Maintenance.oil
        oil_filter = Maintenance.oil_filter
        tran_oil = Maintenance.tran_oil
        air_filter = Maintenance.air_filter
        spark_plug = Maintenance.spark_plug
        chain = Maintenance.chain
        tires = Maintenance.tires
        brakes = Maintenance.brakes
        brake_fluid = Maintenance.brake_fluid
        date = Maintenance.date
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `Maintenance` (`BikeNum`, `Oil`, `OilFilter`, `TranOil`, `AirFilter`, `SparkPlug`, `Chain`, `Tires`, `Brakes`, `BrakeFluid`, `Date`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (bike_num, oil, oil_filter, tran_oil, air_filter, spark_plug, chain, tires, brakes, brake_fluid, date))
                self.connection.commit()
        except Exception as e:
            print(f"Error adding maintenance to the database: {e}")
    
    def get_maintenance(self, bike_num):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `Maintenance` WHERE `BikeNum` = %s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (bike_num))
                result = cursor.fetchall()
                return result if result else None
        except:
            print('Error getting maintenance from database')
    
    def update_maintenance(self, bike_num, Maintenance):
        oil = Maintenance.oil
        oil_filter = Maintenance.oil_filter
        tran_oil = Maintenance.tran_oil
        air_filter = Maintenance.air_filter
        spark_plug = Maintenance.spark_plug
        chain = Maintenance.chain
        tires = Maintenance.tires
        brakes = Maintenance.brakes
        brake_fluid = Maintenance.brake_fluid
        date = Maintenance.date
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE `Maintenance` SET `Oil` = %s, `OilFilter` = %s, `TranOil` = %s, `AirFilter` = %s, `SparkPlug` = %s, `Chain` = %s, `Tires` = %s, `Brakes` = %s, `BrakeFluid` = %s, `Date` = %s WHERE `BikeNum` = %s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (oil, oil_filter, tran_oil, air_filter, spark_plug, chain, tires, brakes, brake_fluid, date, bike_num))
                self.connection.commit()
        except:
            print('Error updating maintenance in database')

    


                
        
    
