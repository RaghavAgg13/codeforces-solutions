for i in range(int(input())):
    n,f,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = a[f-1]
    a.sort(reverse=True)

    if a.index(b)+1 > k:
        print('NO')
    elif a.index(b)+1 <= k < a.index(b)+a.count(b):
        print('MAYBE')
    else:
        print('YES')
