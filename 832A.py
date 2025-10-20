n,k = list(map(int, input().split()))

moves = n//k
print('YES' if moves%2 else 'NO')