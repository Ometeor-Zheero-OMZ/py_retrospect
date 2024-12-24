from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, is_driver: bool = False):
        self.is_driver = is_driver

    @abstractmethod
    def drive(self) -> str:
        pass

class Driver(Person):
    def drive(self) -> str:
        return "grab a handle"
    
class Passenger(Person):
    def drive(self) -> str:
        return "have a seat"

passenger: Person = Passenger()
driver: Person = Driver(True)

class Car:
    def __init__(self, model: str):
        self.model = model
    
    def run(self) -> None:
        print(f"{self.model} iss now running.")

    def ride(self, person: Person) -> str:
        return person.drive()

car = Car("Lightning 0.1")

# Driver should grab a handle
print(f"Driver should {car.ride(driver)}")
# Passenger should have a seat
print(f"Passenger should {car.ride(passenger)}")