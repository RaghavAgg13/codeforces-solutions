for i in range(int(input())):
    n = int(input())
    a = list(input().strip())

    off = a.count("0")
    on = 2*n-off

    if off == 0: print(0, 0)
    else: print(n-off+1, on)