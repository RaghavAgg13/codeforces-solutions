for i in range(int(input())):
    n = int(input())

    a = list(input())
    b = list(input())

    count = 0
    for i in range(n-1, -1, -1):
        if b[i] == '1':
            if a[i] != 'X' and a[i] != '1':
                a[i] = 'X'
                count += 1
            elif i < n-1 and a[i+1] == '1':
                a[i+1] = 'X'
                count += 1
            elif i > 0 and a[i-1] == '1':
                a[i-1] = 'X'
                count += 1
    
    print(count)