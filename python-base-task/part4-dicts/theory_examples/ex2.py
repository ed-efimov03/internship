numbers = map(int, input().split())
even_numbers = {num:"четное" for num in numbers if num % 2 == 0}
print(even_numbers)