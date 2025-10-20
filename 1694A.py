for i in range(int(input())):
    a,b = list(map(int, input().split()))


    c = ''
    for i in range(max(a,b)):
        if i < a:
            print('0', end='')
        if i < b:
            print('1', end='')
    print()