for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    countp = 0
    for i in a: 
        if i >= 0: countp += 1
    
    countn = n-countp
    countp -= a.count(0)

    if (countn%2) or 0 in a:
        print(0)
    else:
        print(1)
        if max(a) > 0:
            print(a.index(max(a))+1, 0)
        else:
            for i in range(n):
                if a[i] < 0:
                        print(i+1, 0, end=' ')
                        break
                