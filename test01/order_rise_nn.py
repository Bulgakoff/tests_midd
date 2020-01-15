# Вывести в порядке возрастания цифры, входящие в десятичную запись натурального числа N.

qwe = 284376489373

qwe = str(qwe)
lst = []
for p in qwe:
    lst.append(int(p))
res = sorted(lst)
print(res)
nn = 284376489373
lst1 = []
while nn > 0:
    qqq = nn % 10
    lst1.append(qqq)
    nn = nn // 10
print(lst1)
www = [45, 7, 89, 65, 4]


def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        # pivot = arr[0]
        low = 0
        high = (len(arr) - 1)
        mid = (low + high) // 2
        pivot = arr[mid]
        less = [p for p in arr if p < pivot]
        more = [p for p in arr if p > pivot]
        return qsort(less) + [pivot] + qsort(more)


res_qsort = qsort(www)
print(res_qsort)
