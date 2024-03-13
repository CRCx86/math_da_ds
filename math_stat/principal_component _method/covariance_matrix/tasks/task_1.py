import numpy as np

salary = np.array([65, 120, 140, 35, 80, 48, 52, 90, 78, 84])
satisfaction = np.array([7, 8, 9, 1, 4, 3, 5, 5, 10, 10])

cov = (salary - salary.mean()) @ (satisfaction - satisfaction.mean()) / (len(salary) - 1)
print(cov)

