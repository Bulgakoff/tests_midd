# Среди натуральных чисел,
# которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
qwe = input('>>>>>>>>>>  ').split()  # 12 13 14 15
ewq = [qwe[i] for i in range(len(qwe)) if qwe[i] == qwe[len(qwe) - 1]]
# for i in range(len(qwe)):
#     if qwe [i] == qwe[len(qwe)-1]:
#         ewq.append(qwe[i])

print(ewq)
num = ['12345566456']


def def_last(qqq):
    lst = []
    for i in range(len(qqq)):
        for j in range(len(qqq[i])):
            lst.append(int(qqq[i][j]))
    return lst


res_def_last = def_last(num)
print(res_def_last)


def recurc(nnn):
    if len(nnn) == 0:
        return 0
    elif len(nnn) == 1:
        return nnn[0]
    else:
        return nnn[0] + recurc(nnn[1:])


res_recurc = recurc(res_def_last)
print(res_recurc)

# n = 1233
# max_s = 0
# max_m = 0
# while n != 0:
#     m = n
#     s = 0
#     while n > 0:
#         s += n % 10
#         n //= 10
#     if s > max_s:
#         max_s = s
#         max_m = m
# print('Число', max_m, 'имеет максимальную сумму цифр:', max_s)
