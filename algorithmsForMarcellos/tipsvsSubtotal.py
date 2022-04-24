from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv('/Users/youngsterethan/Desktop/Marcellos data/SalesByDayCopyFeb2022.csv')
X = data.Total
Y = data.Tips

m, b = np.polyfit(X, Y, 1)
plt.plot(X, m*X+b)
print('Equation: ', str(m) + 'x ' + str(b))

plt.scatter(X,Y)
plt.show()

X = np.array(X)
Y = np.array(Y)
M = len(X)

X = X.reshape((M,1))
reg = LinearRegression()
reg.fit(X,Y)
Y_predic = reg.predict(X)


r2_score = reg.score(X,Y)
print(r2_score)