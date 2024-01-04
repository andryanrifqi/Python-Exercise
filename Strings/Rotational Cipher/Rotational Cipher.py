import string

def rotate(text, key):
    chars = (string.ascii_lowercase)
    cipher = [chars[(index + key) % 26] for index in range(26)]

    chars += chars.upper()
    cipher.extend([char.upper() for char in cipher])

    result = [cipher[chars.index(char)] if char in chars else char for char in text]
    return ''.join(result)