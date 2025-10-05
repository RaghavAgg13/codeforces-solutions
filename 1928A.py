for i in range(int(input())):
    a,b = list(map(int, input().split()))

    if (a//2)*2 == a and a//2 != b: 
        print('YES')
        continue
    if (b//2)*2 == b and b//2 != a:
        print('YES')
        continue

    print('NO')