if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    mx = -101
    mx1 = max(arr)
    for i in arr:
        if i > mx and i < mx1:
            mx = i
    
    print(mx)