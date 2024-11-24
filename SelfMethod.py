
class Vehicle:
    def __init__(vehicle_obj,make,year):
        vehicle_obj.make = make
        vehicle_obj.year = year

v = Vehicle("Suzuki","2022")
print(v.make)