import numpy as np
import scipy.stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

Subs = np.array(sorted(np.random.uniform(0, 20, 2000)))
Money = np.array(sorted(np.random.exponential(1 / 5, 2000)))
Spam = np.array(sorted(np.random.geometric(1 / 5, 2000)))
Work = np.array(sorted(np.random.normal(5, 2, 2000)))

modelSubs_Money = LinearRegression()
modelSubs_Money.fit(Money.reshape(-1, 1), Subs.reshape(-1, 1))
y1 = modelSubs_Money.predict(Money.reshape(-1, 1))
mse1 = mean_squared_error(Subs, y1)
print("MSE первой линейной регрессии равна:", mse1)

print("-" * 50)

modelSubs_Spam = LinearRegression()
modelSubs_Spam.fit(Spam.reshape(-1, 1), Subs.reshape(-1, 1))
y2 = modelSubs_Spam.predict(Spam.reshape(-1, 1))
mse2 = mean_squared_error(Subs.reshape(-1, 1), y2)
print("MSE второй линейной регрессии равна:", mse2)

print("-" * 50)

modelSubs_Work = LinearRegression()
modelSubs_Work.fit(Work.reshape(-1, 1), Subs.reshape(-1, 1))
y3 = modelSubs_Work.predict(Work.reshape(-1, 1))
mse3 = mean_squared_error(Subs, y3)
print("MSE третьей линейной регрессии равна:", mse3)
