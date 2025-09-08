class Car:
    wheels = 4

    # constructor (special method)
    def __init__(self, brand, model):
        self.brand = brand  # instance attribute
        self.model = model

    # method (behavior)
    def drive(self):
        return f"{self.brand} {self.model} is driving!"

# creating objects
car1 = Car("Tesla", "Model S")
car2 = Car("BMW", "X5")

print(car1.drive())  # Tesla Model S is driving!
print(car2.drive())  # BMW X5 is driving!

