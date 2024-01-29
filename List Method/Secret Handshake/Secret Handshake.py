def commands(binary_str):
    secrets = []
    if binary_str[4] == "1":
        secrets.append("wink")
    if binary_str[3] == "1":
        secrets.append("double blink")
    if binary_str[2] == "1":
        secrets.append("close your eyes")
    if binary_str[1] == "1":
        secrets.append("jump")
        
    if binary_str[0] == "1":
        secrets.reverse()
    
    return secrets