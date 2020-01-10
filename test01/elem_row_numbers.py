# Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
n = int(input('========= '))
s = 0
el = 1
arr =[1]
for i in range(n):
    s = s + el
    el = el / -2
    arr.append(el)
res = sum(arr)
print(f'---------------- {arr}')
print(f'---------------- {res}')
# nums = input('>>>>>>>>>  ').split()
# print(nums)  # ['1', '-0.5', '0.25', '-0.125']
# lst_float = [float(p) for p in nums]
# print(lst_float)
# result = sum(lst_float)
# print(result)
# qwe = []
#
#
# def recurs_sum(arr):
#     if len(arr) == 0:
#         return False
#     elif len(arr) == 1:
#         return float(arr[0])
#     else:
#         return float(arr[0]) + recurs_sum(arr[1:])
#
#
# r_recurs_sum = recurs_sum(qwe)
# print(f'>>>>>>>>>>---------{r_recurs_sum}')
