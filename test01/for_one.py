# У вас есть массив чисел.
# Напишите три функции, которые вычисляют сумму этих чисел: с for-циклом,
# с while-циклом, с рекурсией.
qwe = [2345, 45, 456, 78, 89]
print(sum(qwe))
sss = 0
for p in qwe:
    sss += p
print(sss)
s2 = 0
i = 0
while len(qwe) > i:
    s2 += qwe[i]
    i += 1
print(f'----while {s2}')


def recu(qwe):
    if len(qwe) < 2:
        return qwe[0]
    else:
        oth = [p for p in qwe[1:]]
        return qwe[0] + recu(oth)


ree = recu(qwe)
print(ree)
# Вторая задача
# Напишите функцию, которая создаёт комбинацию двух списков таким образом:
# qwe =[1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]
lst1 = [1, 2, 3]
lst2 = [11, 22, 33]
qwe = list(zip(lst1, lst2))
print(qwe)
ewq = []
for p in qwe:
    for j in range(len(p)):
        ewq.append(p[j])
print(ewq)


# Третья задача
# Вычислите первые 100 чисел Фибоначчи. (Напишите код.)0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,..
def fibonacci(n, a=0, b=1):
    yield a
    yield b
    n -= 2
    while n > 0:
        c = a + b
        a = b
        b = c
        yield c
        n -= 1


if __name__ == '__main__':
    for n in fibonacci(20):
        print(n, end=' ')
print()

#         ///////////рекурсия
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f'================== > {fibonacci(10)}')
# Четвёртая задача
# У вас есть массив чисел, составьте из них максимальное число. Например:
#
#  [61, 228, 9] -> 961228
join_to_biggest = lambda a: int(''.join(sorted(map(str, a), reverse=True)))

if __name__ == '__main__':
    print(join_to_biggest([61, 228, 9]))
# join_to_biggest = lambda x: ''.join(sorted(map(str, x), cmp=lambda x, y: cmp(y + x, x + y)))
# Пятая задача
# У вас есть девять цифр: 1, 2, …, 9. Именно в таком порядке.
# Вы можете вставлять между ними знаки «+», «-» или ничего.
# У вас будут получаться выражения вида 123+45-6+7+89. Найдите все из них, которые равны 100.
def all_combinations(a):
    if len(a) <= 1:
        yield a
    else:
        head = ''
        tail = list(a)
        while len(tail) > 0:
            head += tail.pop(0)
            for s in all_combinations(tail):
                yield [head] + s

def all_signs(n):
    if n == 0:
        yield ()
    else:
        for tail in all_signs(n-1):
            for s in '+-':
                yield (s,) + tail

def perform_operations(nums, signs):
    nums = list(map(int, nums))
    result = nums.pop(0)
    n = 1
    for s in signs:
        if s == '+':
            result += nums.pop(0)
        if s == '-':
            result -= nums.pop(0)
        n += 1
    return result

for numbers in all_combinations(tuple(map(str, range(1, 10)))):
    #print(numbers)
    for signs in all_signs(len(numbers) - 1):
        #print(signs)
        summ = perform_operations(numbers, signs)
        if summ == 100:
            print(
                ''.join(map(
                    lambda x: ''.join(x),
                    zip(numbers, signs)))
                + numbers[-1])


qwer = 123+4-5+67-89
print(qwer)