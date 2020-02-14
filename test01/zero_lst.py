qwe = [23, 456, -345, 24, 35, 46, 5, -54, - 5, -6788, 34]
move = len(qwe)
user = int(input('....>>>>>>>>>>>>> : '))
for i in range(abs(user)):
    if user > 0:
        for j in range(move - 1, 0, -1):  # идем справа на лево ++== range(разы,шаг, -1 <направление>)
            qwe[j] = qwe[j - 1]
        qwe[0] = 0
    elif user < 0:
        for j in range(move - 1):  # идем слева на право ++== range(move - 1)
            qwe[j] = qwe[j + 1]
        qwe[move - 1] = 0
    else:
        print('you enter zero - no move')
print(qwe)
