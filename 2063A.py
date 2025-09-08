for i in range(int(input())):
    a,b = list(map(int, input().split()))
    if a == b == 1:
        print(1)
    else: print(b-a)