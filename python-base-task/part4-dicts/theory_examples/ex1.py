str1 = input().split()
str2 = map(int, input().split())
dict_final = dict(zip(str1, str2))
print(dict_final)