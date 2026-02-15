for i in range(int(input())):
    n,s,x = list(map(int, input().split()))
    a = sum(list(map(int, input().split())))

    delta = s-a

    if (delta < 0): print("NO")
    elif not delta%x: print("YES")
    else: print("NO")
    