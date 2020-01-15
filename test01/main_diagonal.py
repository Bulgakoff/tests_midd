# Найти максимальный диагональный элемент и указать его координаты в главной диагонали матрицы.
#
# Также решить задачу для побочной диагонали матрицы.
arr2d = [[2, 3, 4],
         [24, 43, 54],
         [27, 37, 47]]


def pr_matr(lst):
    lst_main_diag = []

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j], end=' ')
            if i == j:
                lst_main_diag.append(lst[i][j])
        print()

    print(lst_main_diag)
    result_max_main = max(lst_main_diag)

    return result_max_main


r_pm = pr_matr(arr2d)
print(r_pm)



def pr_matr(lst):
    lst_notmain_diag = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j], end=' ')
            if i == len(lst) - 1 - j:
                lst_notmain_diag.append(lst[i][j])
        print()

    print(lst_notmain_diag)
    result_max_notmain = max(lst_notmain_diag)

    return result_max_notmain


r_pmm = pr_matr(arr2d)
print(r_pmm)
