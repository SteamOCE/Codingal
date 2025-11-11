from abc import ABC, abstractmethod

class vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        pass

    def info(self):
        print(f"This is a vehicle by {self.brand}")

class Car(vehicle):
    def start_engine(self):
        print(f"The car {self.brand} engine has started")

car1 = Car("Tesla")
car1.info()
car1.start_engine()
