for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))


    counto = []
    counte = []
    for i in range(n):
        if a[i]%2: counto.append(i+1)
        else: counte.append(i+1)

    if (len(counto) >= 1 and len(counte) >= 2):
        print('YES')
        print(counto[0], counte[0], counte[1])
    elif len(counto) >= 3:
        print('YES')
        print(counto[0], counto[1], counto[2])
    else: print('NO')