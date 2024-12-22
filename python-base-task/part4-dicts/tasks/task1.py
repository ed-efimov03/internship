def first_letter_dict(strings: list) -> dict:
    lower_strings = [i.lower() for i in strings]

    letter_dict = dict()

    for i in range(len(strings)):
        string = strings[i]
        letter = strings[i][0].lower()
        if not(letter in letter_dict):
            letter_dict[letter] = [string]
        else:
            letter_dict[letter].append(string)

    return letter_dict
    


strings = ["apple", "dog", "cat", "wine", "country", "cast", "Alpine"]
print(first_letter_dict(strings))

