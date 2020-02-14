# Переставить элементы заданного массива в обратном порядке,
# то есть произвести реверс массива
import random

qwe = [7, 2, 7, 1, 7, 2, 9, 6, 5, 6, 76, 7]
print(qwe)
for i in range(len(qwe) // 2):
    # qwe[i], qwe[len(qwe) - 1 - i] = qwe[len(qwe) - 1 - i], qwe[i]
    qw = qwe[::-1]
print(qw)
