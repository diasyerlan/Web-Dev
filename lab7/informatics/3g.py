n = int(input())

for i in range(2, 30001):
    if n % i == 0:
        print(i)
        break