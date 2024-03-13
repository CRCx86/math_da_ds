import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

comments_length_1 = [38, 81, 81, 65, 50, 43, 44, 55, 32, 26, 69, 136, 2, 19, 76,
                     91, 20, 33, 51, 50, 275, 90, 55, 47, 34, 80, 70, 315, 46,
                     49, 30, 32, 51, 63, 90, 88, 96, 128, 68, 48, 31, 17, 79,
                     18, 52, 84, 26, 95, 25, 180, 37, 34, 25, 59, 34, 69, 278,
                     27, 14, 31, 74, 310, 38, 32, 43, 138, 10, 71, 29, 41, 65,
                     73, 33, 118, 11, 122, 73, 60, 86, 51, 114, 134, 48, 73, 25,
                     34, 60, 90, 22, 321, 238, 30, 82, 94, 55, 80, 144, 34, 106,
                     260, 19, 29, 25, 10, 89, 39, 17, 43, 43, 83, 291, 20, 35, 215,
                     37, 37]

comments_length_2 = [66, 47, 38, 98, 38, 27, 44, 7, 41, 25, 42, 42, 47, 24, 35,
                     20, 20, 8, 32, 14, 41, 19, 21, 53, 27, 5, 21, 42, 41, 21,
                     22, 19, 27, 18, 20, 14, 35, 32, 22, 18, 5, 21, 30, 42, 27,
                     53, 41, 19, 14, 35, 21, 20, 22, 19, 42, 18, 14, 5, 21, 27,
                     27, 21, 53, 20, 104, 29, 71, 44, 105, 42, 10, 21, 45, 33,
                     60, 5, 47, 15, 26, 107, 85, 179, 8, 6, 10, 4, 89, 38, 13]

plt.figure()
plt.subplot(121)
plt.hist(comments_length_1, density=True, bins=40)

plt.subplot(122)
plt.hist(comments_length_2, density=True, bins=20)
plt.show()

log_comments_length_1 = np.log(comments_length_1)
log_comments_length_2 = np.log(comments_length_2)

plt.figure()
plt.subplot(121)
plt.hist(log_comments_length_1, density=True, bins=11)

plt.subplot(122)
plt.hist(log_comments_length_2, density=True, bins=8)
plt.show()

pvalue = stats.ttest_ind(a=log_comments_length_1, b=log_comments_length_2,
                         equal_var=True)[1]

if pvalue < 0.05:
    print("Выборки обладают различными средними")
else:
    print("Выборки могут обладать одинаковыми средними")
