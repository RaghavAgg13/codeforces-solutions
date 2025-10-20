for i in range(int(input())):
    n = int(input())
    a = input()

    sum = int(a[0])
    for i in range(1, n):
        if a[i] == '1':
            print('-' if sum >= 0 else '+', end='')
            sum += -1 if sum >= 0 else 1
        else:
            print('-', end='')
        
    print()