qwe = [2, 3, 5, 6, 7, 98, 5, 3]

print(qwe)


# def evn(arr):
#     even_num = []
#     noeven_num = []
#     for i in range(len(arr)):
#         if arr[i] % 2 == 0:
#             even_num.append(arr[i])
#         elif arr[i] % 2 != 0:
#             noeven_num.append(arr[i])
#     return f' четные {even_num}, не четные {noeven_num}'
# res_evn = evn(qwe)
# print(res_evn)
def index_find(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_ind = i
            return even_ind
        elif arr[i] % 2 != 0:
            odd_ind = i
            return odd_ind


index_res = index_find(qwe)
print(index_res)


# ///////////////////////////////
def select_sort(arr):
    even_lst = []
    odd_lst = []
    for i in range(len(arr)):
        index_res = index_find(qwe)
        if arr[index_res] % 2 == 0:
            even_lst.append(arr.pop(index_res))
        elif arr[index_res] % 2 != 0:
            odd_lst.append(arr.pop(index_res))
    return f'четные {even_lst} нечетные {odd_lst}'


res_select_sort = select_sort(qwe)
print(res_select_sort)
