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

resistor_tolerance = {
        "grey" : "0.05%",
        "violet" : "0.1%",
        "blue" : "0.25%",
        "green" : "0.5%",
        "brown" : "1%",
        "red" : "2%",
        "gold" : "5%",
        "silver" : "10%",
    }

def resistor_label(colors):
    tolerance = ""
    prefix = ""
    
    if len(colors) == 1:
        return "0 ohms"
        
    if len(colors) == 4:
        ohms_value = (resistor_colors[colors[0]]*10 + resistor_colors[colors[1]]) * pow(10, resistor_colors[colors[2]])
        tolerance = resistor_tolerance[colors[3]]
        
    if len(colors) == 5:
        ohms_value = (resistor_colors[colors[0]]*100 + resistor_colors[colors[1]]*10 + resistor_colors[colors[2]]) * pow(10, resistor_colors[colors[3]])
        tolerance = resistor_tolerance[colors[4]]
        
    if ohms_value > 1_000_000_000:
        prefix = "giga"
        ohms_value /= 1_000_000_000
    if ohms_value > 1_000_000:
        prefix = "mega"
        ohms_value /= 1_000_000
    if ohms_value > 1_000:
        prefix = "kilo"
        ohms_value /= 1_000

    if type(ohms_value) is float and ohms_value.is_integer():
        ohms_value = int(ohms_value)
        
    return f"{ohms_value} {prefix}ohms ±{tolerance}"