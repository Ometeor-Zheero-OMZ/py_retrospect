#### 属性

```python
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
        self._is_running = False

    # readonly
    @property
    def run(self):
        return self._is_running

    @run.setter
    def run(self, is_running: bool):
        if isinstance(is_running, bool):
            self._is_running = is_running
            if is_running:
                print(f"{self.model} is now running.")
            else:
                print(f"{self.model} has stopped.")
        else:
            raise ValueError("run must be a boolean value.")

    def check_version(self):
        print(f"{self.version} of {self.brand_name}'s {self.model} released in {self.released_date}")

spark_01 = HondaCar("Spark 0.1", "0.1.0", "2024-12-24", "Honda")

# Spark 0.1 is now running.
spark_01.run = True
# Spark 0.1 has stopped.
spark_01.run = False

# 0.1.0 of Honda's Spark 0.1 released in 2024-12-24
spark_01.check_version()
```
