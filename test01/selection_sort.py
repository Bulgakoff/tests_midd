lll = [3, 7, 45, 8, 9, 4, 6, 8]

# def find_smallest_index(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
#
#
# def selec_sort(arr):
#     qwe = []
#     for i in range(len(arr)):
#         r = find_smallest_index(arr)
#         qwe.append(arr.pop(r))
#     return qwe
#
#
# res_selec_sort = selec_sort(lll)
# print(res_selec_sort)
lll = [3, 7, 45, 8, 9, 4, 6, 8]


def selec_index(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            ind_ev = i
            return ind_ev
        else:
            ind_odd = i
            return ind_odd


# ///////////////////////////////////////////
def even_sort(arr):
    arr_even = []
    arr_odd = []
    for i in range(len(arr)):
        value_even_odd_index = selec_index(arr)
        res_pop_value = arr.pop(value_even_odd_index)
        if res_pop_value % 2 == 0:
            arr_even.append(res_pop_value)
        else:
            arr_odd.append(res_pop_value)

    return f'четные  ==  {arr_even}  нечетные == {arr_odd}'


res_even_sort = even_sort(lll)
print(res_even_sort)
