for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if a.count(1)%2 == b.count(1)%2: print('Tie')
    else:
        for i in range(n-1, -1, -1):
            if a[i] != b[i]:
                print("Ajisai" if i%2 == 0 else 'Mai')
                break
