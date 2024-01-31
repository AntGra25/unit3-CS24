# Quiz038

## 1. Solution

```.py
import random
from matplotlib import pyplot as plt


class SalemanMap:
    def __init__(self):
        self.x = []
        self.y = []
        self.names = None

    def generate_data(self, names: list[str]):
        self.names = names

    def get_map(self):
        for i in range(len(self.names)):
            self.x.append(random.randint(0, 100))
            self.y.append(random.randint(0, 100))
        plt.scatter(self.x, self.y, c='red')
        plt.xlabel('Distance (km)')
        plt.ylabel('Distance (km)')
        plt.xlim(0, 100)
        plt.ylim(0, 100)
        for i in range(len(self.names)):
            plt.annotate(self.names[i], (self.x[i], self.y[i]))
        plt.show()
            

Map = SalemanMap()
Map.generate_data(['Sapporo', 'Fukuoka', 'Nagoya', 'Kobe', 'Kawasaki',
                   'Osaka', 'Kyoto', 'Saitama', 'Yokohama', 'Tokyo'])
print(Map.get_map())
```
## 2. Proof of Work

![Quiz038](https://github.com/AntGra25/unit3-CS24/assets/142757981/7abb4847-7fff-4b96-92f2-8ba51b96c815)


## 3. UML Diagram

![Quiz038C](https://github.com/AntGra25/unit3-CS24/assets/142757981/1617703e-24bc-4042-97ba-66aad2611234)

