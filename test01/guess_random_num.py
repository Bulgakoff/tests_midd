# Угадать случайное число
# В программе генерируется случайное целое число от 0 до 100.

# Пользователь должен его отгадать не более чем за 10 попыток.

# После каждой неудачной попытки должно сообщаться больше или
# меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
from random import randint

number = randint(0, 101)
min_start = 0
max_fin = 100
print(number)
i = 0
while i < 3:
    i += 1
    print(f'попытка № {i}')
    answer = int(input('Введите число '))
    if answer < number:
        min_start = answer
        print(f'использована {i} попытка ответ меньше пробуем еще ')
    elif answer > number:
        max_fin = answer
        print(f'использована {i} попытка  ответ больше загаданного пробуем еще ')
    else:
        print(f'использована {i} попытка  вы угадали ')
        break
else:
    print('закончились попытки')