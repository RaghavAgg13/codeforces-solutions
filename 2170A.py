for i in range(int(input())):
    n = int(input())

    ans = 0
    for i in range(n):
        for j in range(1, n+1):
            sum = i*n+j

            if i+1 < n: sum += (i+1)*n+j
            if i-1 >= 0: sum += (i-1)*n+j
            if j+1 <= n: sum += i*n+j+1
            if j-1 >= 1: sum += i*n+j-1

            ans = max(ans, sum)
    
    print(ans)