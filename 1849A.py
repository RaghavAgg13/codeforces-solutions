for i in range(int(input())):
    b,c,h = list(map(int, input().split()))

    l1, l2 = b, c+h
    if l1 > l2:
        print(2*l2+1)
    else:
        print(2*l1-1)