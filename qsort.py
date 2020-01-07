qwe = [6, 50, 5, 44, 982, 4, 5, 2, 4, 56, 7, 8, 9, 93, 5, 6, 7, 8]


def qsort(lst):
    if len(lst) < 2:
        return lst  # базовый случай !!! смотря что возвращать здесь подумать ---
    # либо элемент списка(когда арифм дейтвия), либо индекс (когда порядок вычисляется),
    # либо массив-список целиком когда бысрая сортировка ("разделяй и властвуй")
    else:
        pivot = lst[0]
        less = [p for p in lst[1:] if pivot > p]
        more = [p for p in lst[1:] if pivot < p]
        return qsort(less) + [pivot] + qsort(more)


res_qsort = qsort(qwe)
print(res_qsort)
