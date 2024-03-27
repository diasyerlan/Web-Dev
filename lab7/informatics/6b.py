def power(a: int, b: int):
    return a ** b

a = input().split()

print(power(float(a[0]), float(a[1])))