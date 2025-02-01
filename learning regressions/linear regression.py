
import pandas as pn
import matplotlib.pyplot as plt

#first I'll start doing a simple linear regression of just two variables (x,y), with random variables that change every time. 

import numpy as np
num_puntos = 30
x = np.random.randint(0,100, num_puntos)
y = np.random.randint(0,100, num_puntos)

print("Lista puntos:")
print(x,y)

def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points[i].studytime
        y = points[i].score
        total_error += (y - (m * x + b)) ** 2
    total_error / float(len(points))
def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points[i]
        y = points[i]

        m_gradient += -(2/n) * x * (y -(m_now * x + b_now))
        b_gradient += -(2/n) * x * (y -(m_now * x + b_now))

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m, b

m = 0
b = 0
L = 0.0001
epochs = 1000

for i in range(epochs):
    if i % 50 == 0:
        print(f"Epoch: {i}")
    m, b = gradient_descent(m, b, (x,y), L)
print (m, b)

plt.scatter(x, y, color="black")
plt.plot(list(range(20, 80)), [m * x + b for x in range(20, 80)], color="red")
plt.show()


