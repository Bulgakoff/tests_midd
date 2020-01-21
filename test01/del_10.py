# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.
lst_even_range = [0] * 8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            lst_even_range[j - 2] = lst_even_range[j - 2] + 1
i = 1
for p in lst_even_range:
    i += 1
    print(f'элемент {p} повторяется {i} раз')

print(lst_even_range)
a = [0] * 8
print(a)
