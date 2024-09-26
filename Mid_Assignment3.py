class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def drive(self, a):
        self.a = a
        return self.a + self.mileage

    def __str__(self):
        return f"The {self.color} car has {self.drive(100)} miles"


car1 = Car("blue", 0)
car2 = Car("red", 10)
car3 = Car("purple", 20)

print(car1)
print(car2)
print(car3)

print()
