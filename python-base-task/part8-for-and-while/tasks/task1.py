import random

lenght_password = int(input("Длина пароля: "))
type_symbols = input("Тип символов: ")

numbers = [chr(i + ord('0')) for i in range(10)]
letters = [chr(i + ord('a')) for i in range(26)] + [chr(i + ord('A')) for i in range(26)]
spec_symbols = [chr(i + ord('!')) for i in range(15)] + [chr(i + ord(':')) for i in range(7)]

password = ""


if type_symbols.strip().lower()  == "буквы":
    for i in range(lenght_password):
        password += random.choice(letters)

elif type_symbols.strip().lower() == "буквы и цифры":
    number = random.choice(numbers)
    letter = random.choice(letters)
    password_symbols_list = [number, letter]

    for i in range(lenght_password - 2):
        password_symbols_list.append(random.choice(numbers + letters))
    
    for i in range(lenght_password):
        symbol = random.choice(password_symbols_list)
        password += symbol
        password_symbols_list.remove(symbol)
    
elif type_symbols.strip().lower() == "буквы, цифры и специальные символы":
    number = random.choice(numbers)
    letter = random.choice(letters)
    spec_symbol = random.choice(spec_symbols)
    password_symbols_list = [number, letter, spec_symbol]

    for i in range(lenght_password - 3):
        password_symbols_list.append(random.choice(numbers + letters + spec_symbols))
    
    for i in range(lenght_password):
        symbol = random.choice(password_symbols_list)
        password += symbol
        password_symbols_list.remove(symbol)
else:
    print("Извините, такой команды нет")

print(password)
