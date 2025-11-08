for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    diff = []
    for i in range(1, n):
        if a[i]< a[i-1]:
            diff.append(a[i-1]-a[i])
            a[i] = a[i-1]
    
    
    diff.sort()
    l = len(diff)
    s = sum(diff)+diff[-1] if diff != [] else 0

    print(s)