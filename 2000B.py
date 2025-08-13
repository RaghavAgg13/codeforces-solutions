for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = True
    possible = set()
    if a[0]+1 <= n: possible.add(a[0]+1)
    if a[0]-1 >= 1: possible.add(a[0]-1)
    
    for i in a[1:]:
        if i in possible:
            if i+1 <= n: possible.add(i+1)
            if i-1 >= 1: possible.add(i-1)
        else:
            b = False
            break

    print('YES' if b else 'NO')