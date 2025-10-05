for i in range(int(input())):
    a,b,c,d = list(map(int, input().split()))

    if min(a,c) >= min(b,d): print('Gellyfish')
    else: print('Flower')