import re

string = input().split()
regex = r'\wкруж\w'


for i in string:
    if re.search(regex, i):
        print(i)