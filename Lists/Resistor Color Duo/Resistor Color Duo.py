resistor_colors = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]
    
def value(colors):

    return int(str(resistor_colors.index(colors[0])) + str(resistor_colors.index(colors[1])))