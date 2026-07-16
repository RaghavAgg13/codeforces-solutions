n,m = list(map(int, input().split()))

prev = -1
ans = True
for i in range(n):
    a = input()

    if (len(set(list(a))) > 1): ans = False
    if (a[0] == prev): ans = False

    prev = a[0]

print("YES" if ans else "NO")