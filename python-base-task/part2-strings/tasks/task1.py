def frequency(file_name: str) -> dict: 
    f = open(file_name, 'r')
    content = f.read()
    words = content.split()

    dict_words = dict()

    for i in range(len(words)):
        old_word = words[i]

        new_word = ""
        for i in range(len(old_word) - 1, -1, -1):
            if old_word[i].isalnum():
                new_word = old_word[:i + 1]
                break

        for i in range(len(new_word)):
            if new_word[i].isalnum():
                new_word = new_word[i:]
                break    

        new_word = new_word.lower()

        if new_word in dict_words:
            dict_words[new_word] += 1
        else:
            dict_words[new_word] = 1

    dict_words = dict(sorted(dict_words.items()))

    print(dict_words)
    f.close()

file_name = "text.txt"

frequency(file_name)