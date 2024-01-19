import re
encoder = str.maketrans("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba")
decoder = str.maketrans("zyxwvutsrqponmlkjihgfedcba", "abcdefghijklmnopqrstuvwxyz")
atbash_len = 5

def encode(plain_text):
    text = re.sub("[^A-Z0-9]", "", plain_text,0,re.IGNORECASE).lower().translate(encoder)
    return " ".join(text[i:i+atbash_len] for i in range(0, len(text), atbash_len))

def decode(ciphered_text):
    return ciphered_text.replace(" ", "").lower().translate(decoder)