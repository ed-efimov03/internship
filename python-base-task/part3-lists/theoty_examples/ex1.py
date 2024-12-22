string = "5rff09832ejwfdew09f034"
lst_numbers_string = [int(i) for i in string if i.isdigit()]
print(max(lst_numbers_string))
print(min(lst_numbers_string))
print(sum(lst_numbers_string))