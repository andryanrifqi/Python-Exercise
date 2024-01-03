def is_valid(isbn):
    chars = list(char for char in isbn if char.isalnum())
    if len(chars) != 10:
        return(False)
    if chars[-1] == 'X':
        chars[-1] = '10'
    numbers = list(char for char in chars if char.isdigit())
    if len(numbers) != 10:
        return(False)
    count = 10
    out = 0
    for number in numbers:
        out += int(number)*count
        count -= 1  
    return(out%11 == 0)