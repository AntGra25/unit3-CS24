# Quiz034

## 1. Solution
```.py
from matplotlib import pyplot as plt

x_out = []
y_out = []
negx_out = []
negy_out = []
x = 0
for i in range(101):
    y = (x-2)**2
    x_out.append(x)
    y_out.append(y)
    negx_out.append(-x)
    negy_out.append(-y)
    x += 0.06

plt.style.use('ggplot')
plt.plot(negx_out, y_out, color='red', label='Parabola 1')
plt.plot(x_out, y_out, color='blue', label='Parabola 2')
plt.plot(negx_out, negy_out, color='purple', label='Parabola 3')
plt.plot(x_out, negy_out, color='gray', label='Parabola 4')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Four Funny Parabolas')
plt.legend()
plt.xlim([-16, 16])
plt.show()

```

## 2. Proof of Work
![Quiz034](https://github.com/AntGra25/unit3-CS24/assets/142757981/95187e86-8856-4769-a3a2-38f55ebd2834)

