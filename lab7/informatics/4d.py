n = int(input())

i = 0
ok = False
while 2 ** i <= n:
    if 2 ** i == n:
        print("YES")
        ok = True
        break
    i += 1

if not ok:
    print("NO")