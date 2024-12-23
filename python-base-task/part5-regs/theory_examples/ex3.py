import re

string = input()
regex = r'[\!\?\.\,\"\:\;]'

res = re.sub(regex, '', string)
print(res)