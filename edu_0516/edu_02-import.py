# from car import Car2
# from car import ElecCar
from car import *

myCar2 = Car2("audi", "a2", 2024, "green")
print(myCar2)
print(myCar2.get_descriptive_name())

myCar2.color = "red"
myCar2.update_odometer(80)
myCar2.read_odometer()

Car2.count += 5
print(f"클래스 변수 출력 : {Car2.count}")
Car2.printing()

my_elec_car = ElecCar("tesla", "model x", 2022, "red")
print(my_elec_car.get_descriptive_name())
print(my_elec_car.battery.battery_capa())
