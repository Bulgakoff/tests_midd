# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
# надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
import random

qwe = [56]*8
qw = []
# qw = [i for i in range(len(qwe)) if qwe[i] % 2 == 0]
for i in range(8):
    qwe[i] = random.randint(1, 9)
    # qwe.append(random.randint(1, 9))
for i in range(len(qwe)):
    if qwe[i] % 2 == 0:
        qw.append(i)
print(qwe)
print(qw)