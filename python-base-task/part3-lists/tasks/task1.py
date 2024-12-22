import random

def func(arr: list) -> list:
    arr_new = [i for i in arr if i >= 0]
    arr_new.sort(reverse=True)
    return arr_new

arr_list = [random.randint(-10, 10) for _ in range(20)]
print(arr_list)
print(func(arr_list))