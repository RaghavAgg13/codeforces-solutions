for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    odd = sum([i%2 for i in a])
    even = n-odd

    if not odd%2 and not even%2:
        print('YES')
    elif not (odd-even)%2:
        check = False
        for i in range(n):
            if a[i]-1 in a or a[i]+1 in a:
                check = True
                break
        print('YES' if check else 'NO')
    else: print('NO')