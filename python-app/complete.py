from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    def __init__(self, brand, fuel, capacity):
        self.brand = brand
        self.__fuel = fuel         # Encapsulation: private
        self.speed = 0
        self.capacity = capacity   # max passengers or load
        self.status = "idle"       # current status

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        self.speed = 0
        self.status = "stopped"
        print(f"{self.brand} stopped.")

    def get_fuel(self):
        return self.__fuel

    def refuel(self, amount):
        self.__fuel += amount
        print(f"{self.brand} refueled to {self.__fuel}L.")

    def info(self):
        print(f"Brand: {self.brand}, Fuel: {self.__fuel}L, Capacity: {self.capacity}, Status: {self.status}")

    @abstractmethod
    def accelerate(self):
        pass

# Car class
class Car(Vehicle):
    wheels = 4  # class attribute

    def start(self):
        if self.get_fuel() > 0:
            self.status = "running"
            print(f"{self.brand} Car started with a key.")
        else:
            print(f"{self.brand} Car cannot start, no fuel!")

    def accelerate(self):
        if self.get_fuel() > 0:
            self.speed += 10
            self.__consume_fuel()
            self.status = "running"
            print(f"{self.brand} Car accelerating. Speed: {self.speed} km/h")
        else:
            print(f"{self.brand} Car cannot accelerate, no fuel!")

    def __consume_fuel(self):
        self._Vehicle__fuel -= 1  # private fuel consumption

# Bike class
class Bike(Vehicle):
    wheels = 2

    def start(self):
        if self.get_fuel() > 0:
            self.status = "running"
            print(f"{self.brand} Bike started with a button.")
        else:
            print(f"{self.brand} Bike cannot start, no fuel!")

    def accelerate(self):
        if self.get_fuel() > 0:
            self.speed += 5
            self.__consume_fuel()
            self.status = "running"
            print(f"{self.brand} Bike accelerating. Speed: {self.speed} km/h")
        else:
            print(f"{self.brand} Bike cannot accelerate, no fuel!")

    def __consume_fuel(self):
        self._Vehicle__fuel -= 0.5

# Truck class
class Truck(Vehicle):
    wheels = 6

    def start(self):
        if self.get_fuel() > 0:
            self.status = "running"
            print(f"{self.brand} Truck started with ignition key.")
        else:
            print(f"{self.brand} Truck cannot start, no fuel!")

    def accelerate(self):
        if self.get_fuel() > 0:
            self.speed += 8
            self.__consume_fuel()
            self.status = "running"
            print(f"{self.brand} Truck accelerating. Speed: {self.speed} km/h")
        else:
            print(f"{self.brand} Truck cannot accelerate, no fuel!")

    def __consume_fuel(self):
        self._Vehicle__fuel -= 2  # trucks consume more fuel

    def calculate_delivery_cost(self, distance, rate_per_km=2):
        cost = distance * rate_per_km
        print(f"Delivery cost for {distance} km: ${cost}")
        return cost

# Real-world usage
fleet = [
    Car("Tesla", 10, 5),
    Bike("Yamaha", 5, 2),
    Truck("Volvo", 50, 10000)
]

for v in fleet:
    v.info()
    v.start()
    v.accelerate()
    v.accelerate()
    v.stop()
    v.refuel(5)
    if isinstance(v, Truck):
        v.calculate_delivery_cost(120)
    print("-"*40)
