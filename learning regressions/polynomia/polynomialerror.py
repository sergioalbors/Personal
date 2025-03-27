import numpy as np
import matplotlib.pyplot as plt

#we want to see how error changes depending on the type of regression we use, ideally
#our error should be 0 but that is quite close to imposible so we seek the lowest error possible.
#Now we'll compare if polynomial regression fits best to this function

x = np.arange(-10,10, 0.1)
y = 2*(x**3) + 1*(x**2)+ 1*(x) + 1 #same fucntion than last example
y_noise = 150 * np.random.normal(size=len(x)) #same noise too
y = y + y_noise
plt.scatter(x , y)

n = len(x)
x1 = x 
x2 = np.power(x1, 2)
x3 = np.power(x1, 3)
x_bias = np.ones((n,1))
x1 = x1.reshape(-1, 1)
x2 = x2.reshape(-1, 1)
x3 = x3.reshape(-1, 1)

x_new = np.append(x_bias, x1, axis=1)   
x_new = np.append(x_bias, x2, axis=1)
x_new = np.append(x_bias, x3, axis=1)
x_new_transpose = np.transpose(x_new)
x_new_transpose_dot_x_new = x_new_transpose.dot(x_new)
temp_1 = np.linalg.inv(x_new_transpose_dot_x_new)
temp_2 = x_new_transpose.dot(y)
theta = temp_1.dot(temp_2)
print(theta)
beta_0 = theta[0]
beta_1 = theta[1]
beta_2 = theta[2]
beta_3 = theta[3]

plt.scatter(x, y)
plt.plot(x, beta_0 + beta_1*x1 + beta_2*x2 + beta_3*x3,c = "black")
plt.show()
