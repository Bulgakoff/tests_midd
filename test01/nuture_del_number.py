# Вывести на экран, из каких простых множителей состоит введенное натуральное число.
n = 2014
# lst_n = []
# for i in range(1, n + 1):
#     lst_n.append(i)
#
# for i in range(1, len(lst_n)):
#     if n % lst_n[i] == 0:
#         print(lst_n[i], end=' ')

# def recu_nut_num():
#     pass
# res_rnn =recu_nut_num()
#
#
#
while n > 1:
    i = 2
    f = 0
    while 1:
        if n % i == 0:
            n = n // i
            print(i, end=' ')
            f = 1
            break
        else:
            i += 1
    if f == 1:
        continue
print()
