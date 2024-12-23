import re

string = input()
regex = re.compile(r'\b\w+\-\w+\b')
res = regex.findall(string)
print(res)