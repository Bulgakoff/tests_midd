# Найти сумму элементов между минимальным и максимальным элементами массива
# В одномерном массиве найти сумму элементов, находящихся между минимальным
# и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
qwe = [5, 54, 5, 4,5,7,8,33,66,55, 4, 75, 4]
qqq = max(qwe)
www = min(qwe)
ima = qwe.index(qqq)
imi= qwe.index(www)
print (f'макс числа {qqq} индекс == {ima }')
print (f'мин числа {www} индекс == {imi }')

rty_1=[]
rty_2=[]
if ima < imi:
    for p in qwe[ima+1:imi]:
        rty_1 .append(p)
    print (f'сумма равна {sum(rty_1 )}')

elif ima > imi:
    for p in qwe[imi+1:ima]:
        rty_2 .append(p)
    print (f'сумма равна {sum(rty_2 )}')