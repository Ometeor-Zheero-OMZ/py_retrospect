class Car:
    def __init__(self, model, version, released_date):
        self.model = model
        self.version = version
        self.released_date = released_date

    def update(self, version):
        self.version = version

    __update = update

class HondaCar(Car):
    def __init__(self, model, version, released_date, brand_name):
        super().__init__(model, version, released_date)
        self.brand_name = brand_name

    def run(self):
        print(f"{self.model} is now running.")
    
    def check_version(self):
        print(f"{self.version} of {self.brand_name}'s {self.model} released in {self.released_date}")

spark_01 = HondaCar("Spark 0.1", "0.1.0", "2024-12-24", "Honda")

# Spark 0.1 is now running.
spark_01.run()

# 0.1.0 of Honda's Spark 0.1 released in 2024-12-24
spark_01.check_version()