# Найдите сумму и количество элементов массива,
# попавших в интервал [a; b]. Границы интервала вводятся с клавиатуры.
arrr = [5, 3, 4, 6, 7, -4, 4, 6, 4, -55, 4, -3, 5, 45, 6, 5, 56, -554]
arrr = sorted(arrr)
n_start = 1
n_fin = 10
lst = []
for p in arrr:
    if n_fin >= p >= n_start:
        lst.append(p)
print(lst)
# lst = [i for i in range(n_start, n_fin + 1)]
# print(lst)
# # def recu(arr):
# #     if len(arr) == 1:
# #         return arr[0]
# #     else:
# #         return arr[0] + recu(arr[1:])
# # res_recu = recu(lst)
# # print(res_recu)
# res = sum(lst)
# print(res)
