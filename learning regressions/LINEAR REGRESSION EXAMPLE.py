#LINEAR REGRESSION EXAMPLE   

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("C:\\Users\\salbo\\Desktop\\Personal\\learning regressions\\regressiondata.csv")
x = data["STUDYTIME"].astype(float)
y = data["SCORE"].astype(float)

m = 0.98898371
b = 1.9175

yi = m * x + b
plt.scatter(x,y)
plt.plot(x, yi, linestyle='-', color="red", label=f"y = {m}x + {b}")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("First example of a linear regression")
plt.show()