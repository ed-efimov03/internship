def sorted_words(string: str) -> str:
    words = string.upper().split() 
    unique_words = sorted(list(set(words)))
    return unique_words

print(sorted_words(input()))