# Случайные числа в диапазоне от -5 до 5 разложить по двум массивам:
# в одни помещать только положительные, во второй - только отрицательные.
# Числа, равные нулю, игнорировать.
# Вывести на экран все сгенерированные случайные числа и элементы обоих массивов.
import random

lst_nn_len = []
i = -5
while i <= 5:
    lst_nn_len.append(i)
    i += 1
print(lst_nn_len)
aaa = []
for i in range(len(lst_nn_len)):
    nn = random.randint(-5, 5)
    aaa.append(nn)
print(aaa)
# ///////////////////////
qwe = []
ewq = []
for p in aaa:
    if p < 0:
        qwe.append(p)
    elif p > 0:
        ewq.append(p)

print(qwe)
print(ewq)
