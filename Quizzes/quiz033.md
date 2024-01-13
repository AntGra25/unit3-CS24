# Quiz033

## 1. Solution
```.py
from matplotlib import pyplot as plt

plt.style.use('ggplot')

x_out = []
y_out = []
negx_out = []
negy_out = []
x = -2
for i in range(101):
    y = x ** 2
    y_out.append(y)
    x_out.append(x)
    negy_out.append(-y)
    negx_out.append(-x)
    x += 0.04

plt.plot(x_out, y_out, color='red', label='Parabola 1 (x-axis)')
plt.plot(x_out, negy_out, color='blue', label='Parabola 2 (x-axis)')
plt.plot(y_out, x_out, color='purple', label='Parabola 3 (y-axis)')
plt.plot(negy_out, x_out, color='gray', label='Parabola 4 (y-axis)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.title('Four Parabolas Aligned with Axes')
plt.show()
```

## 2. Proof of Work
![Quiz033](https://github.com/AntGra25/unit3-CS24/assets/142757981/40ac2be1-cfe5-4047-8373-3a64b3d4adc5)

