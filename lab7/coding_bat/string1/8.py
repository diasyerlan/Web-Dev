def left2(s):
    if len(s) <= 2:
        return s

    return s[2:] + s[:2]
