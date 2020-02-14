import random

N = 15
m = random.randint(-15, 50)
arr = [m]
i = 1
while i < N:
    m = random.randint(-15, 50)
    f = 1
    for j in arr:
        if abs(j) == abs(m):
            f = 0
            break
    if f == 1:
        arr.append(m)
        i += 1
print(arr)
j = 0
for i in range(1, 15):
    if abs(arr[i]) > abs(arr[j]):
        j = i
print('Максимальный по модулю %d-й элемент равен %d' % (j, arr[j]))
