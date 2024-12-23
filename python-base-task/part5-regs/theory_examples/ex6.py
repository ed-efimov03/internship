import re
regex = re.compile(r'(?P<имя>[^,]+),(?P<фамилия>[^,]+),(?P<математика>[^,]+),(?P<физика>[^,]+),(?P<химия>[^,]+),(?P<биология>[^,]+)')
lst = []
n = int(input())
for i in range(n):
    string = input()
    res = regex.search(string).groupdict()
    lst.append(res)
print(lst)