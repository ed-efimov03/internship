n = int(input())
pr = 1
while n != 0:
    pr *= n % 10
    n //= 10
    print(pr, n)