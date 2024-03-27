def prime(a: int):
    for i in range(2,int(a ** 0.5) + 1):
        if a % i == 0:
            return "composite"
    
    return "prime"

a = int(input())

print(prime(a))