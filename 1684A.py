for i in range(int(input())):
    a = list(input().strip())
    n = len(a)

    if n == 2: print(a[1])
    else: print(min(a))