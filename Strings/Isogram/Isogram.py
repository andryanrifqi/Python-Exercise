def is_isogram(string):
    chars = ''.join(char for char in string if char.isalnum()).lower()
    return len(chars)  == len(set(chars))