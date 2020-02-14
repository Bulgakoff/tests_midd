# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

rlst = [4] * 8

for i in range(len(rlst)):
    rlst[i] = random.randint(1, 9)
print(rlst)
mi = min(rlst)
ma = max(rlst)
print(mi, ma)
index_mi = rlst.index(mi)
index_ma = rlst.index(ma)
print(index_mi, index_ma)
rlst[index_ma], rlst[index_mi] = rlst[index_mi], rlst[index_ma]
print(rlst)
