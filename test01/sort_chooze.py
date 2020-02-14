import random

n = 10


def rand_mtx(nn):
    qwe_lst = []
    for i in range(nn):
        qwe_lst.append(random.randint(1, 50))
    return qwe_lst


res_rand_mtx = rand_mtx(n)
print(res_rand_mtx)


def sort_choo(lll):
    if len(lll) < 2:
        return lll
    else:
        pivot = lll[0]
        less = [p for p in lll if p < lll[0]]
        right = [p for p in lll if p > lll[0]]
        result = sort_choo(less) + [pivot] + sort_choo(right)
        return result


res_sort_choo = sort_choo(res_rand_mtx)
print(res_sort_choo)


def sort_max_ind(lst):
    if len(lst) < 2:
        return lst
    else:
        min_el = lst[0]
        for i in range(len(lst)):
            if min_el > lst[i]:
                min_el = lst[i]
        return min_el


res_sort_max_ind = sort_max_ind(res_rand_mtx)
print(f'-----------min_el---------->{res_sort_max_ind}')
