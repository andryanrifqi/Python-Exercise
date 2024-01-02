def is_isogram(string):
    chars = ''.join(char for char in string if char.isalnum()).lower()
    for char in chars:
        if (chars.count(char) <= 1) == False:
            return False
    return True