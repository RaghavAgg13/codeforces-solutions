for i in range(int(input())):
    n = int(input())
    a = list(input().split())

    arr = []
    for i in range(12):
        arr.append(a.count(str(2**i)))
    
    for i in range(11):
        arr[i+1] += arr[i]//2

    print("YES" if arr[11] >= 1 else 'NO')