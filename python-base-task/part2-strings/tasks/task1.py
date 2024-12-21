def frequency(fn): 
    f = open(fn, 'r')
    content = f.read()
    words = content.split()

    dict_words = dict()

    for i in range(len(words)):
        word = words[i]

        clean_word = ""
        for letter in word:
            if letter.isalnum():
                clean_word += letter 

        words[i] = clean_word.lower()

        word = words[i]

        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1

    dict_words = dict(sorted(dict_words.items()))

    print(dict_words)
    f.close()

file_name = "text.txt"

frequency(file_name)