for i in range(int(input())):
    n,k = list(map(int, input().split()))
    
    count0 = k//2
    if (n+1-k)%2: count0 += k%2

    print('NO' if count0%2 else 'YES')