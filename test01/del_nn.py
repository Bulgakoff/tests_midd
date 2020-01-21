# Из натурального числа удалить заданную цифру. Число и цифру вводить с клавиатуры.
#
# Например, задано число 5683. Требуется удалить из него цифру 8. Получится число 563.
nn = '5683'
n_del = '8'
nn_int_str = [p for p in nn]
if n_del in nn_int_str:
    nn_int_str.remove(n_del)
print(nn_int_str)
nn_fin = ''.join(nn_int_str)
print(nn_fin)
