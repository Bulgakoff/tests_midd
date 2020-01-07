qwe = [6, 50, 5, 3, 5, 53]


def qsort_merge(lst):
    if len(lst) < 2:
        return lst
    else:
        low = 0
        high = len(lst) - 1
        mid = (low + high) // 2
        pivot = lst[mid]
        less = [p for p in lst if pivot > p]
        more = [p for p in lst if pivot < p]
        return qsort_merge(less) + [pivot] + qsort_merge(more)


res_qsort_merge = qsort_merge(qwe)
print(res_qsort_merge)
