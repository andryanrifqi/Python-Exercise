def is_valid(isbn):
    chars = list(char for char in isbn if char.isalnum())
    if len(chars) != 10:
        return False
    if chars[-1] == 'X':
        chars[-1] = '10'
    if not all(char.isdigit() for char in chars):
        return False
    count = 10
    total = 0
    for char in chars:
        total += int(char) * count
        count -= 1  
    return total % 11 == 0