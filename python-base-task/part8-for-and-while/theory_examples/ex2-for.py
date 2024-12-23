numbers = map(int, input().split())
c, pr = 0, 1
maxi = -1000
mini = 1000
for n in numbers:
    if n > 0:
        c += 1
    elif n < 0:
        pr *= n
    if n > maxi:
        maxi = n
    if n < mini:
        mini = n
print(c, pr, mini, maxi, sep='\n')