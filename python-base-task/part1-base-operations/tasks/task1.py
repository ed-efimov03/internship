numbers = list(map(int, input().split()))
min_number = min(numbers)
max_number = max(numbers)
diff = max_number - min_number
print(min_number, max_number, diff)
