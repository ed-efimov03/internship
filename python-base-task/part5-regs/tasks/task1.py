import re
file_name = 'text1.txt'
f = open(file_name, 'r')
content = f.read()
regex = re.compile(r'\b[\w.+-]+@[\w-]+[\.\w+]*\.\w+\b')
mails = regex.findall(content)
f.close()
print(mails)

