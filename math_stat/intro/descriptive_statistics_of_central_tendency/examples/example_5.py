from scipy import stats
import numpy as np

# Самостоятельно зададим выборку.
x = np.array([1, 1, 2, 0, -1, 0, 0, 0, 0])

mode_value = stats.mode(x)
print(mode_value)  # -> ModeResult(mode=array([0]), count=array([5]))

print(mode_value.mode)  # -> [0]
# print(mode_value.mode[0])  # -> 0
#
print(mode_value.count)  # -> [5]
# print(mode_value.count[0])  # -> 5
