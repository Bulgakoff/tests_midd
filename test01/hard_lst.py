# Дан одномерный массив, состоящий из натуральных чисел.
# Выполнить сортировку данного массива по возрастанию суммы цифр чисел.
# Например, дан массив чисел [14, 30, 103]. После сортировки он будет таким: [30, 103, 14],
# так как сумма цифр числа 30 составляет 3, числа 103 равна 4, числа 14 равна 5.
#
# Вывести на экран исходный массив, отсортированный массив, а также для контроля сумму цифр
# каждого числа отсортированного массива.

# qwe = [1234, 456, 1234, 465, 798]
# sss =[]
# for p in qwe:
#     sss.append(str(p))
# print(sss)
# qqq =[]
# for i in range(len(sss)):
#     inter = []
#     for j in range(len(sss[i])):
#         inter.append(int(sss[i][j]))
#     qqq.append(inter)
# print(qqq)
# aaa=[]
# for p in qqq:
#     aaa.append(sum(p))
# print(aaa)
# www = sorted(aaa)
# print(www)

# ////////////////////
xxx = [61, 228, 9]
ppp = []
for p in xxx:
    ppp.append(str(p))
print(ppp)
qwe = []
for i in range(len(ppp)):
    inter = []
    for j in range(len(ppp[i])):
        inter.append(int(ppp[i][j]))
    qwe.append(inter)
print(qwe)
fff =[]
for i in range(len(qwe)):
    j = len(qwe)
    mmm = 0
    while qwe:
        if qwe[i][0]>mmm:
            fff.append(qwe.pop(i))
            j -=1
print(fff)

