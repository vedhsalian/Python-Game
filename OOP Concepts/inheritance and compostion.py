class Vehicle:
    def __init__(self,wheels=0,color="",people=0):
        self.vw=wheels
        self.vc=color
        self.vp=people

    def __get_vehicle_type(self):
        if self.vw==2:
            print("The type is a bike")
        elif self.vw==4:
            print("The type is a car")


class Car(Vehicle):
    def __init__(self,brand,type,mileage,wheels,color,people):
        self.cb=brand
        self.ct=type
        self._cm=mileage
        super().__init__(wheels,color,people)

class Electric_car(Car):
    def __init__(self,brand,type,mileage,wheels,color,people,battery_capacity,charging_time,range):
        self.ebc=battery_capacity
        self.ect=charging_time
        self.er=range
        super().__init__(brand,type,mileage,wheels,color,people)

vehicle1=Vehicle(4,"red",5)
print(vehicle1.vp)
vehicle2=Vehicle()
print(vehicle2.vp)
vehicle1._Vehicle__get_vehicle_type()

car1=Car("BMW","SUV",500,4,"blue",6)
print(car1.vc)

electric_car1=Electric_car("Tesla","Sedan",500,4,"white",5,75,"120 mins",450)
print(electric_car1.ct)
print(electric_car1.ect)
print(electric_car1._cm)