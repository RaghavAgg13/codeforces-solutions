for i in range(int(input())):
    a,b = list(map(int, input().split()))

    if a == b:
        print('0')
    elif a > b:
        if (a-b)%2 == 0: print('1')
        else: print('2')
    else: # a < b
        if (b-a)%2 == 0: print('2')
        else: print('1')