def is_valid(isbn):
    chars = list(char for char in isbn if char.isalnum())
    if len(chars) != 10:
        return False
    if chars[-1] == 'X':
        chars[-1] = '10'
    if not all(char.isdigit() for char in chars):
        return False
        
    return sum(int(a) * b for a,b in zip(chars, range(10, 0, -1))) % 11 == 0