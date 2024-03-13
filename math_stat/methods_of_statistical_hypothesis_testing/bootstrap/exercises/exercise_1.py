import numpy as np

n = 100

X = np.random.normal(100, 20, n)

k = 1000 #число выборок бутстрепа
f = n #размер выборки бутстрепа

#Ваш код
bs_std = []
i = 0
while i < k:
    bs_val = np.random.choice(X, f, True)
    std = np.std(bs_val, ddof=1)
    bs_std.append(std)
    i += 1

std = np.std(X, ddof=1)
bs_st = np.std(bs_std, ddof=1)

print(std)
print(bs_st)
