# Quiz050

## 1. Solution
```.py
class Flight:
    def __init__(self, flight_number: str, origin: str, destination: str, departure_time: str, duration: list[int]):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.duration = duration

    def get_duration(self):
        return f"{self.duration[0]} hours {self.duration[1]} minutes and {self.duration[2]} seconds"

    def get_info(self):
        return f"Flight {self.flight_number} from {self.origin} to {self.destination} departs at {self.departure_time} and lasts {self.get_duration()}"


flight1 = Flight(flight_number="AA123", origin="New York", destination="Los Angeles", departure_time="10:00 AM", duration=[5, 30, 3])
flight2 = Flight(flight_number="UH123", origin="Narita", destination="Naha", departure_time="3:15 PM", duration=[2, 45, 30])
print(flight1.get_info())
print(flight2.get_info())

```
## 2. Proof of Work
![Quiz050](https://github.com/AntGra25/unit3-CS24/assets/142757981/15d929d9-657c-4724-87c5-d856c2fcd780)

## 3. UML Diagram
![Quiz050C](https://github.com/AntGra25/unit3-CS24/assets/142757981/c9d9bab7-4e97-4702-8005-a103f0723c97)
