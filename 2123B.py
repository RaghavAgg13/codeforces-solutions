for i in range(int(input())):
    n,j,k = list(map(int, input().split()))
    l = list(map(int, input().split()))

    score = l[j-1]
    l.sort(reverse=True)
    
    weaker = 0
    for i in range(n):
        if l[i] < score: weaker += 1

    # number of people to eliminate == n-k
    # either n-stronger
    print('YES' if weaker >= n-k else 'NO')