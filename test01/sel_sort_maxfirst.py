squares = [0, 81, 1, 36, 444, 9, 64, 16, 25]


def qwe(arr):
    biggest_value = arr[0]
    biggest_index = 0
    for i in range(len(arr)):
        if biggest_value < arr[i]:
            biggest_value = arr[i]
            biggest_index = i
    return biggest_index


res_qwe = qwe(squares)

print(f'индекс максимального значения == {res_qwe}')


def select_sortMax(arr):
    arrr = []

    for i in range(len(arr)):
        q = qwe(arr)
        w = arr.pop(q)
        arrr.append(w)
    return arrr


res_select = select_sortMax(squares)

print(res_select)
