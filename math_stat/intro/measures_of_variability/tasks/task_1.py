import numpy as np

x = np.array([4.6, 3.0, 3.2, 4.2, 5.0])

var_v = np.sqrt(np.var(x, ddof=1))

print(var_v)
