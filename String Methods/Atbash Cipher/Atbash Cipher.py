import re
from string import ascii_lowercase

KEY = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])
atbash_len = 5

def encode(plain_text):
    text = re.sub("[^A-Z0-9]", "", plain_text,0,re.IGNORECASE).lower().translate(KEY)
    return " ".join(text[i:i+atbash_len] for i in range(0, len(text), atbash_len))

def decode(ciphered_text):
    return ciphered_text.replace(" ", "").lower().translate(KEY)