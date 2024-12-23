import re

string = input()
regex = r'(\d{4})/(\d{2})/(\d{2})'
new_regex = r'\3/\2/\1'
res = re.sub(regex, new_regex, string)

print(res)