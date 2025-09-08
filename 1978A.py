for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    if a[-1] != max(a): print(max(a)+a[-1])
    else:
        a.sort(reverse=True)
        print(a[0]+a[1])