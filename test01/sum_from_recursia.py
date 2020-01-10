qwe = [1, 2, 4, 0, 4, 6]

lst = [1,2]


def recursion_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + recursion_sum(arr[1:])# рекурсивно берем срез кроме перврого элемента


res = recursion_sum(lst)
print(res)

# def no_recurs_sum(lst):
#     total = 0
#     for p in lst:
#         total = total + p
#     return total
#
#
# res_no_recurs_sum = no_recurs_sum(qwe)
# print(res_no_recurs_sum)
