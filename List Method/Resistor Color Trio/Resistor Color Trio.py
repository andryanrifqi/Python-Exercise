resistor_colors = {
        "black" : 0,
        "brown" : 1,
        "red" : 2,
        "orange" : 3,
        "yellow" : 4,
        "green" : 5,
        "blue" : 6,
        "violet" : 7,
        "grey" : 8,
        "white" : 9,
    }

def label(colors):
    ohms_value = list(str((resistor_colors[colors[0]]*10 + resistor_colors[colors[1]]) * pow(10, resistor_colors[colors[2]])))
    if ohms_value[0] == '0':
        return '0 ohms'
    
    counter = 0
    while ohms_value[-1] == '0':
        ohms_value.pop(-1)
        counter += 1

    if counter == 0:
        ohms_value.append(' ohms')
    if counter == 1:
        ohms_value.append('0 ohms')
    if counter == 2:
        ohms_value.append('00 ohms')
    if counter == 3:
        ohms_value.append(' kiloohms')
    if counter == 4:
        ohms_value.append('0 kiloohms')
    if counter == 5:
        ohms_value.append('00 kiloohms')    
    if counter == 6:
        ohms_value.append(' megaohms')
    if counter == 7:
        ohms_value.append('0 megaohms')
    if counter == 8:
        ohms_value.append('00 megaohms')
    if counter == 9:
        ohms_value.append(' gigaohms')
    if counter == 10:
        ohms_value.append('0 gigaohms')
    
    
    return ''.join(ohms_value)