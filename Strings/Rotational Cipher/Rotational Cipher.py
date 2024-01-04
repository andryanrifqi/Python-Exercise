import string

def rotate(text, key):
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)
    
    if 0 < key < 26:
        cipher = list(text)
        indx_in = 0
        for char in cipher:
            if not char.isalpha():
                indx_in += 1
            if char in alphabet_lower:
                indx_out = alphabet_lower.index(char) + key
                if indx_out > 25:
                    indx_out = indx_out - 26
                cipher[indx_in] = alphabet_lower[indx_out]
                indx_in += 1
            if char in alphabet_upper:
                indx_out = alphabet_upper.index(char) + key
                if indx_out > 25:
                    indx_out -= 26
                cipher[indx_in] = alphabet_upper[indx_out]
                indx_in += 1
        return ''.join(cipher)
    return text