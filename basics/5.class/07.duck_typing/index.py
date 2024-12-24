class Person:
    def __init__(self, is_driver=False):
        self.is_driver = is_driver

    def drive(self) -> str:
        if self.is_driver:
            return "grab a handle"
        else:
            return "have a seat"

passenger = Person()
driver = Person(True)

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