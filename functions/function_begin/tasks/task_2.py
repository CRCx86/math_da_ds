import numpy as np
from matplotlib import pyplot as plt

data = np.array([[  1, 2500, 1500, 5200, 9200, 1200, 1500, 21100],
                [  2, 2630, 1200, 5100, 6100, 2100, 1200, 18330],
                [  3, 2140, 1340, 4550, 9550, 3550, 1340, 22470],
                [  4, 3400, 1130, 5870, 8870, 1870, 1130, 22270],
                [  5, 3600, 1740, 4560, 7760, 1560, 1740, 20960],
                [  6, 2760, 1555, 4890, 7490, 1890, 1555, 20140],
                [  7, 2980, 1120, 4780, 8980, 1780, 1120, 20760],
                [  8, 3700, 1400, 5860, 9960, 2860, 1400, 25180],
                [  9, 3540, 1780, 6100, 8100, 2100, 1780, 23400],
                [  10, 1990, 1890, 8300, 10300, 2300, 1890, 26670],
                [  11, 2340, 2100, 7300, 13300, 2400, 2100, 29540],
                [  12, 2900, 1760, 7400, 14400, 1800, 1760, 30020]])

months = data[:, 0]
sums = data[:, 7]

plt.plot(months, sums)