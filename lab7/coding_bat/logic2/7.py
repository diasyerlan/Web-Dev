def close_far(a, b, c):
    def is_close(x, y):
        return abs(x - y) <= 1
    
    def is_far(x, y):
        return abs(x - y) >= 2
    
    if (is_close(b, a) and is_far(c, a) and is_far(c, b)) or \
       (is_close(c, a) and is_far(b, a) and is_far(b, c)):
        return True
    return False