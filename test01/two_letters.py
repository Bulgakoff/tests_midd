import random
import functools

# Посчитать четные и нечетные цифры числа

# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
qwe = input('-------->  ')
ewq = []
for p in qwe:
    ewq.append(int(p))
r1 = [p for p in ewq if p % 2 == 0]
r2 = [p for p in ewq if p % 2 != 0]
print(f' r1 == {r1} == {len(r1)} четных числа в {qwe}')
print(f' r1 == {r2} == {len(r2)} не четных числа в {qwe}')

re1 = list(filter(lambda p: p % 2 == 0, ewq))
print(f'==========>{re1}')
