# Сжать массив, удалив из него все элементы,
# величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.
qwe = [23, 456, -345, 24, 35, 46, 5, -54]
eee = sorted(qwe)  # [-345, -54, 5, 23, 24, 35, 46, 456]
print(eee)
print(f'len1 == {len(qwe)}')
print(f'-------start-qwe- {qwe}')
n = len(qwe)
zzz = []
low = int(input('>>>>>> 1'))
high = int(input('>>>>>> 2'))
n = len(eee)
i = 0
while i < n:
    j = 0
    while j < n:
        if low <= eee[j] <= high:
            zzz.append(eee.pop(j))
            n -= 1
        else:
            j+=1
    i+=1
print(f'len2 == {len(eee)}')
print(f'--removed-----zzz-- {zzz}')
print(f'-------fin- eee- {eee}')
for i in range(len(zzz)):
    eee.append(0)
print(eee)
