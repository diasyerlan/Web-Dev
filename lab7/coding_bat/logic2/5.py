def round_sum(a, b, c):
    def round10(num):
        remainder = num % 10
        if remainder >= 5:
            return num + (10 - remainder)
        else:
            return num - remainder
    
    return round10(a) + round10(b) + round10(c)