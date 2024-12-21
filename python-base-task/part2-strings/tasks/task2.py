string = input()
string_without_strip = string.replace(' ', '')
clean_string = ""
for letter in string_without_strip:
    if letter.isalnum():
        clean_string += letter
print(clean_string == clean_string[::-1])