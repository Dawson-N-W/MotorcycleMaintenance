from dataclasses import dataclass
import datetime

@dataclass
class Maintenance:
    oil: bool = False
    oil_filter: bool = False
    tran_oil:bool = False
    air_filter:bool = False
    spark_plug:bool = False
    chain:bool = False
    tires:bool = False
    brakes:bool = False
    brake_fluid:bool = False
    date = datetime.datetime.now()
    