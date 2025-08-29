n = int(input())
a = list(map(int, input().split()))

first = a[0]
last = a[-1]
print(a[1]-first, last-first)
for i in range(1, n-1):
    print(min(a[i]-a[i-1], a[i+1]-a[i]), max(a[-1]-a[i], a[i]-first))
print(last-a[-2], last-first)