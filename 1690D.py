for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = input()

    if a == 'W'*n:
        m = k
    elif a == 'B'*n:
        m = 0
    elif 'B'*k in a:
        m = 0
    else:
        noOfB = [a[:k].count('W')]
        for i in range(k, n):
            noOfB.append(noOfB[-1]+1 if a[i] == 'W' else noOfB[-1])
            noOfB[-1] -= 1 if a[i-k] == 'W' else 0
        m = min(noOfB)

    print(m)