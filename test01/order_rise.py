# Вывести в порядке возрастания цифры,
# входящие в десятичную запись натурального числа N.
nn = input('>>>>>>>>>>>  ').split()
nn_lst = sorted([int(p) for p in nn])
nn_str_lst = [str(p) for p in nn_lst]
nn_str_join = ''.join(nn_str_lst)
print(type(nn_str_join))