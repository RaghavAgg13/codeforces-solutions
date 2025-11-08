from sys import stdin
input = stdin.readline

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    prefix = [a[0]]
    s = sum(a)
    suffix = [s]
    for i in range(1, n):
        prefix.append(prefix[-1]+a[i])
        suffix.append(s-prefix[i-1])
    
    idx = 0
    suffix_seen = set()
    for i in range(n-1, -1, -1):
        if i+1 < n:
            suffix_seen.add(suffix[i+1])

        if prefix[i] in suffix_seen:
            idx = i+1+suffix[::-1].index(prefix[i])+1
            break
    
    print(idx)