# Quiz037

## 1. Solution

```.py
class CompoundInterest:
    def __init__(self, principal, rate, number_of_years):
        self.principal = principal
        self.rate = rate
        self.number_of_years = number_of_years

    def calculate(self):
        return self.principal * (1 + (self.rate/100)) ** self.number_of_years


class Accounting(CompoundInterest):
    def __init__(self, customer_name, customer_email, principal, rate, number_of_years):
        super().__init__(principal, rate, number_of_years)
        self.customer_name = customer_name
        self.customer_email = customer_email

    def calculate_interest(self):
        return (f"{self.customer_name} will have {self.calculate():.2f} USD in {self.number_of_years} years if the "
                f"principal is {self.principal}USD with {self.rate}% annual interest")


account = Accounting(customer_name='Ms Sato', customer_email='sato@xy.z', principal=100, rate=10, number_of_years=10)
print(account.calculate_interest())
```
## 2. Proof of Work

![Quiz037](https://github.com/AntGra25/unit3-CS24/assets/142757981/c010d9c5-0e65-4f4a-842f-b0b249042c36)

## 3. UML Diagram
