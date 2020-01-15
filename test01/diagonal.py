
for i in range(4):
    for j in range(4):
        if i == j or i == 3-j:
            print('w', end=' ')
        else:
            print('<', end=' ')
    print()
