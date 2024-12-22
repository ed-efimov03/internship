lst_numbers_string = list(map(int, input().split()))
new_list = [i for i in lst_numbers_string if lst_numbers_string.count(i) > 1]
print(*new_list)