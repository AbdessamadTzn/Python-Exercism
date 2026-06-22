def response(hey_bob):
    if not hey_bob.strip():
        return "Fine. Be that way!"
    if hey_bob.strip()[-1] == '?' and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob.strip()[-1] == '?':
        return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."
