lst = [1, 2, 234, 5, 56]


def lst_count_items(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + lst_count_items(arr[1:])


result = lst_count_items(lst)
print(result)
