from abc import ABC, abstractmethod
import zipfile


class ElectricVehicleRecord(ABC):

    def __init__(self,region,parameter,powertrain,year,unit,value):
        self.region = region
        self.parameter = parameter
        self.powertrain = powertrain
        self.year = year
        self.unit = unit

    def display(self):
        pass

class EVSalesRecord(ElectricVehicleRecord):

    def display(self):
        print(f"{self.region}: {self.parameter}: {self.powertrain}:{self.year}: {self.unit} ")