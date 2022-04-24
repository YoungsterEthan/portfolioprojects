from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

hitters = pd.read_csv('topbatters.csv')

#setting lists and arrays
X = hitters.OBP
Y = hitters.OPS


#creating regression line
m, b = np.polyfit(X, Y, 1)
plt.plot(X, m*X+b)
print('Equation: ', str(m) + 'x ' + str(b))

plt.scatter(X,Y)
plt.show()
#creating model
X = np.array(X)
Y = np.array(Y)
M = len(X)

X = X.reshape((M,1))
reg = LinearRegression()
#fitting training data
reg = reg.fit(X,Y)
#Y prediction
Y_pred = reg.predict(X)

r2_score = reg.score(X,Y)
print(r2_score)
print("Predict:", reg.predict(0.390))