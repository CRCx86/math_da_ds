import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

X = [1546.07326743, 1586.56337911, 4107.9247858, 1870.4330324, 8021.3758974,
     1516.78573082, 1628.15249286, 2117.75240781, 829.34424151, 4362.06016599,
     4560.36970634, 2029.31109361, 2099.85972157, 2345.47389303, 4990.13620728,
     2019.83311777, 3460.93252924, 2637.9404186, 3123.31101043, 4579.52788905,
     3552.24308212, 1979.72074512, 4062.15861921, 2925.53339485, 6009.41452041,
     3118.69061871, 3862.68743002, 2454.87557981, 3000.24891436, 2295.10889191]
Y = [28.12970705, 210.1902005, 81.54515259, 31.571036, 45.82595509,
     72.08836875, 39.54674948, 35.45275113, 156.35601147, 78.11146533,
     18.23504806, 26.3728256, 22.67476352, 44.74310987, 64.55990754,
     123.34774546, 60.43715297, 83.91068249, 50.07668644, 283.40050724,
     68.49570864, 74.6011155, 14.10654579, 140.64466074, 13.8039958,
     41.22101815, 110.36824261, 153.93959758, 31.83783785, 81.95677535]

pvalue = 0  # переменная для сохранения p-value

# Ваш код тут
LogX = np.log(X)
LogY = np.log(Y)

pvalue = stats.ttest_ind(a=LogX, b=LogY, equal_var=True)[1]
print(pvalue)

if pvalue < 0.05:
    print("Выборки обладают различными средними.")
else:
    print("Выборки могут обладать одинаковыми средними.")
