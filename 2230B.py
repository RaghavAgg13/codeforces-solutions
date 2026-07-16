for _ in range(int(input())):
    a = list(input())
    n = len(a)

    cnt = 0
    for i in range(n):
        if a[i] == '4':
            cnt += 1
            a[i] = '-1'

    ones = 0
    for i in range(n):
        if a[i] == '1' or a[i] == '3':
            ones += 1

    twos = 0
    ans = ones

    for i in range(n-1, -1, -1):
        if a[i] == '2':
            twos += 1
        elif a[i] == '1' or a[i] == '3':
            ones -= 1

        if ones+twos < ans:
            ans = ones+twos
    
    print(cnt + ans)