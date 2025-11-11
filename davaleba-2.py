from abc import ABC, abstractmethod
import zipfile


class ElectricVehicleRecord(ABC):

    def __init__(self,region,parameter,powertrain,year,unit,value):
        self.region = region
        self.parameter = parameter
        self.powertrain = powertrain
        self.year = int(year)
        self.unit = unit
        self.value = float(value)

    @abstractmethod
    def display(self):
        pass

class EVSalesRecord(ElectricVehicleRecord):

    def display(self):
        print(f"{self.region}: {self.parameter}: {self.powertrain}:{self.year}: {self.unit}: {self.value}")
    @staticmethod 
    def recordebis_analizi(records, **filters):
        result = []
        for rec in records:
            match = True
            for key,value in filters.items():
                if hasattr(rec, key):
                    attr = getattr(rec,key)


                    if isinstance(value,tuple) and len(value) == 2:
                        if not (value[0] <= attr <= value[1]):
                            match = False
                            break
                    else:
                        if attr != value:
                            match = False
                            break
                
                else:
                    match = False
                    break
            
            if match:
                result.append(rec)
        return result

class EVStockShareRecord(ElectricVehicleRecord):
    @staticmethod
    def display(self):
        print(f"{self.year} - {self.region} - {self.parameter} - {self.powertrain} - {self.value} - {self.unit}")

    def recordebis_analizi(records, **filters):
        return EVSalesRecord.recordebis_analizi(records,**filters)
    

def read_zip_data(zip_path):
    records=[]
    with zipfile.ZipFile(zip_path, 'r')as z:
        for filename in z.namelist():
            with z.open(filename) as f:
                for line in f:
                    decoded = line.decode('utf-8').strip()
                    fields = decoded.split("#@#")
                    if len(fields) == 6:
                        region, parameter, powertrain, year,unit,value = fields
                        if parameter.lower() == "ev sales":
                            rec = EVSalesRecord(region, parameter, powertrain,year,unit,value)
                        else:
                            rec = EVStockShareRecord(region,parameter,powertrain,year,unit,value)
                        records.append(rec)

    return records

if __name__ == "__main__":
    yvela_recordi = read_zip_data("cars.zip")

    filtered1 = EVSalesRecord.recordebis_analizi(
        yvela_recordi,
        region = "Australia",
        unit = "percent",
        year = (2012, 2015)
    )
    print(f"Australia 2012-2015, percent rekistraciebis raodenoba: {len(filtered1)}")

    filtered2 = EVSalesRecord.recordebis_analizi(
        yvela_recordi,
        parameter="EV sales",
        powertrain = "BEV",
        unit = "Vehicles"
    )

    filtered2 = [rec for rec in filtered2 if rec.value<1]
    print(f"EV sales, BEV, Vehicles value <1 rekistraciebis raodenoba: {len(filtered2)}")