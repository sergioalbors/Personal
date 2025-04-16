import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.1)
y = 2*(x**3) + 1*(x**2)+ 1*(x) + 1
y_noise = 150 * np.random.normal(size=len(x))
y = y + y_noise
 
x.shape
n = len(x)
x_bias = np.ones((n,1))
x_bias.shape
x = np.reshape(x,(n,1))
x_new= np.append(x_bias,x,axis=1)
x_new_transpose = np.transpose(x_new)
x_new_transpose_dot_x_new = x_new_transpose.dot(x_new)
temp_1 = np.linalg.inv(x_new_transpose_dot_x_new)
temp_2 = x_new_transpose.dot(y)
theta = temp_1.dot(temp_2)
plt.scatter(x,y)
plt.plot(x, theta[0]+theta[1]*x)
plt.title("Sergioalbors(l.r)")
plt.show()
def prediction(x,intercept, slope):
    y_pred = x*slope + intercept
    return y_pred
pred = prediction(x,theta[0],theta[1])
def err(y_pred, y):
    var = (y - y_pred)
    var = var*var
    n = len(var)

    MSE = var.sum()
    MSE = MSE/n
    return MSE
error = err(pred,y)
print(error)
