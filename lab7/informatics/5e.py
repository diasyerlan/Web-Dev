n = int(input())
a = input().split()

cnt = 0
ok = False
for i in range(1, n):
    if int(a[i]) > 0 and int(a[i - 1]) > 0:
        print("YES")
        ok = True
        break
    if int(a[i]) < 0 and int(a[i - 1]) < 0:
        print("YES")
        ok = True
        break

if not ok:
    print("NO")