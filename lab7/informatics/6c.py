def xor(a: int, b: int):
    if a != b:
        return 1
    return 0

a = input().split()

print(xor(float(a[0]), float(a[1])))