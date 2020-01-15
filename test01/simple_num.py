from math import sqrt

count = 10
for i in range(10):
    n = int(input())
    for j in range(2, int(sqrt(n)) + 1):
        if n % j == 0:
            count -= 1
            break

print(count)