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
    ohms_value = (resistor_colors[colors[0]]*10 + resistor_colors[colors[1]]) * pow(10, resistor_colors[colors[2]])
    prefix = ""
    
    if ohms_value > 1_000_000_000:
        prefix = "giga"
        ohms_value //= 1_000_000_000
    if ohms_value > 1_000_000:
        prefix = "mega"
        ohms_value //= 1_000_000
    if ohms_value > 1_000:
        prefix = "kilo"
        ohms_value //= 1_000
        
    return f"{ohms_value} {prefix}ohms"