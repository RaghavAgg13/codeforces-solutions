for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if min(a)%2:
        print('YES')
    else:
        check = False
        for i in a:
            if i%2:
                check = True
                break
        print('YES' if not check else 'NO')