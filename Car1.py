import Automobile

class Car1(Automobile):

        def __init__(self, make, model, mileage, price, doors):
            self.doors = doors

        def set_doors(self, doors):
            self.doors = doors

        def get_doors(self):
            return self.doors

mycar = Car1("Audi", "2007", 12500, 21500.0, 4)

print("make", mycar.getMake())

print("model", mycar.getModel())

print("mileage", mycar.getMileage())

print("price", mycar.getPrice())

print("doors", mycar.getDoors())