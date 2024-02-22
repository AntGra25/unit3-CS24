# Quiz052

## 1. Solution
```.py
import math

class Wheel:
    def __init__(self, size: int):
        self.size = size

    def get_size(self):
        return f"Wheel size: {self.size} inches"

    def get_perimeter(self):
        return 3.14 * self.size

    def get_km_per_rotation(self):
        rotations = math.ceil(1 / (self.get_perimeter() * 2.54 * 10 ** -5))
        return f"Rotations per km: {rotations}"


class Bicycle:
    def __init__(self, material: str, wheels: Wheel):
        self.material = material
        self.wheels = wheels

    def ride(self):
        return f"{self.wheels.get_size()}; Frame material: {self.material}"


test_wheel = Wheel(size=26)
test_bicycle = Bicycle(material="aluminum", wheels=test_wheel)

print(test_bicycle.ride())
print(test_wheel.get_km_per_rotation())

```

## 2. Proof of Work
![Quiz052](https://github.com/AntGra25/unit3-CS24/assets/142757981/608ba8a8-3dd6-46c4-a18a-70766caa141b)

## 3. UML Diagram
![Quiz052C](https://github.com/AntGra25/unit3-CS24/assets/142757981/c75df0d9-50b7-4fd1-8b20-4ed355df1fab)
