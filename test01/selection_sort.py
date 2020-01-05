lll = [3, 7, 45, 8, 9, 4, 6, 8]


def find_smallest_index(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selec_sort(arr):
    qwe = []
    for i in range(len(arr)):
        r = find_smallest_index(arr)
        qwe.append(arr.pop(r))
    return qwe


res_selec_sort = selec_sort(lll)
print(res_selec_sort)