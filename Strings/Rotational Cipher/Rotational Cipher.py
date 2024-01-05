import string

def rotate(text, key):
    chars = (string.ascii_lowercase)
    
    new_chars = chars[key:] + chars[:key]
    cipher = str.maketrans((chars + chars.upper()), (new_chars + new_chars.upper()))
    return text.translate(cipher)