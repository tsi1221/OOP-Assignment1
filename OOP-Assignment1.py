class Vehicle:
    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed

    def get_name(self):
        return self.__name

    def get_speed(self):
        return self.__speed

    def move(self):
        print(f"{self.__name} is moving at {self.__speed} km/h")

class Car(Vehicle):
    def move(self):
        print(f"{self.get_name()} is driving on the road 🚗 at {self.get_speed()} km/h")

class Plane(Vehicle):
    def move(self):
        print(f"{self.get_name()} is flying in the sky ✈️ at {self.get_speed()} km/h")

car1 = Car("Toyota Corolla", 120)
plane1 = Plane("Boeing 747", 900)

vehicles = [car1, plane1]

for vehicle in vehicles:
    vehicle.move()
