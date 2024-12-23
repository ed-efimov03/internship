import re

string = input()
regex = r'\bко{1,2}'
res = re.findall(regex, string, re.I)
print(len(res))
