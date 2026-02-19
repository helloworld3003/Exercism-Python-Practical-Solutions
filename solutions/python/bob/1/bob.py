def response(hey_bob):
    if hey_bob.strip().endswith("?") and hey_bob==hey_bob.upper() and any(c.isalpha() for c in hey_bob):
        return "Calm down, I know what I'm doing!"
    elif hey_bob.strip().endswith("?"):
        return "Sure."
    elif hey_bob.strip()=="" or hey_bob==None:
        return "Fine. Be that way!"
    elif hey_bob==hey_bob.upper() and any(c.isalpha() for c in hey_bob  ):
        return "Whoa, chill out!"
    else:
        return "Whatever."
