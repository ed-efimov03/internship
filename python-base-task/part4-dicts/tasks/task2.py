string = list(input())
dictionary = {letter: string.count(letter) for letter in string}
print(dictionary)
