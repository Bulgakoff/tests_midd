my_list = [1, 2, 34, 45, 6, 7, 8, 5, 34, 55, 66, 7, 0, 555, 777, 888, 8990]
num = 6
my_list_sorted = sorted(my_list)
print(my_list_sorted)


def binn_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > item:
            high = mid - 1
        elif arr[mid] < item:
            low = mid + 1
        else:
            print(f' значение найдено item == {arr[mid]}')
            return arr[mid]


res_binn_search = binn_search(my_list_sorted, num)
print(res_binn_search)
