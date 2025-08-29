import bisect
n,m = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))

print(*[bisect.bisect_right(a, i) for i in b])