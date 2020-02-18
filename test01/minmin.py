# некоторые числа кратные числу 7 , приделении на 2,3,4,5,6 дают остаток 1.
# найти миним из таких чисел

import random

qwe = [w for w in range(random.randint(1, 100))]
print(qwe)
sss = [p for p in qwe if p % 7 == 1]
print(sss)


def minbimn(sss):
    min = sss[0]
    i = 0
    while i < len(sss):
        if sss[i] < min:
            min = sss[i]
        i += 1
    return min


print(minbimn(sss))
