# Допишите код здесь.
import numpy as np

visitors = [3500, 5800, 5200, 7000, 6800, 6400]
orders = [52, 82, 61, 103, 112, 104]
time = [133, 122, 104, 109, 120, 124]

visitors = np.array(visitors)
orders = np.array(orders)
time = np.array(time)

cov = (visitors - visitors.mean()) @ (orders - orders.mean()) / (len(visitors) - 1)
cov_1 = (visitors - visitors.mean()) @ (time - time.mean()) / (len(orders) - 1)
cov_2 = (orders - orders.mean()) @ (time - time.mean()) / (len(time) - 1)

cov_mat = np.array([
    [np.var(visitors, ddof=1), cov, cov_1],
    [cov, np.var(orders, ddof=1), cov_2],
    [cov_1, cov_2, np.var(time, ddof=1)],
])
print("Матрица ковариации:")
print(cov_mat)

array = np.array([visitors, orders, time])
cov_mat = np.cov(array)
print("Матрица ковариации:")
print(cov_mat)
