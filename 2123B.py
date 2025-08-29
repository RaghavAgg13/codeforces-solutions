import bisect
for i in range(int(input())):
    n,j,k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    if (n-k)%2 == 0 or j == max(l) or k == n:
        print('YES')
    else: print('NO')