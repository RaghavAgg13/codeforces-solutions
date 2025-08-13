for i in range(int(input())):
    n,m = list(map(int, input().split()))
    if n == 1: print('0')
    else:
        print(m-n)