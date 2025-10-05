for z in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    check = 1
    freq = [0]*k
    for i in a:
        freq[i%k] += 1

    for i in range(k):
        if freq[i] == 1:
            check = 0
            print('YES')
            for j in range(n):
                if a[j]%k == i:
                    print(j+1)
            break
    
    if check: print('NO')