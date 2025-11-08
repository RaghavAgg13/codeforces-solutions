n,m,a,b = list(map(int, input().split()))

print(min((m-n%m)*a, (n%m)*b))