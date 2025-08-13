for i in range(int(input())):
    a,b,c = list(map(int, input().split()))

    a += (c+1)//2
    b += (c)//2

    print('First' if a > b else 'Second')