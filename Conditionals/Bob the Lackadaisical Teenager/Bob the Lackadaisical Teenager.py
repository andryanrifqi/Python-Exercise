def response(hey_bob):
    
    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob.rstrip(" ").endswith("?"):
        return "Sure."
    if hey_bob.isspace() or len(hey_bob) == 0:
        return "Fine. Be that way!"

    return "Whatever."