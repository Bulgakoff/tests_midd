lst = [1, 2, 4, 5, 4, 3, 2, 3]


def recurs_sum(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + recurs_sum(arr[1:])


res_recurs_sum = recurs_sum(lst)
print(res_recurs_sum)
