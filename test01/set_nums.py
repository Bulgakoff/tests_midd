# Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
nums = 4
nums1 = nums*(nums+1)/2
print(f'---------{nums1}')
def s_left(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
        print(i, end=' ')
    return s


res_s_left = s_left(nums)
print(f'========== {res_s_left}')


def s_right():
    pass


res_s_right = s_right()
print(res_s_right)
