class Dog:
    species = "Canis Lupus Familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def description(self):
        return f"{self.name} is {self.age} years old and is a/n {self.breed}"

    def __str__(self):
        return f"{self.name} is {self.age} years old and is a/n {self.breed}"

    def speak(self, sound):
        return print(f"{self.name} says {sound}")

chi = Dog("Chi", 3, "Shihtzu")
klin = Dog("Klin", 2, "Bulldog")

# Practice Activity 1

coffee = Dog("Coffee", 5, "Aspin")
print("Name       : ", coffee.name)
print("Age        : ", coffee.age)
print("Breed      : ", coffee.breed)
print("Species    : ", coffee.species)
print("Description: ", coffee.description())
coffee.speak("Hello~!")

print(chi)
print(klin)
print()
