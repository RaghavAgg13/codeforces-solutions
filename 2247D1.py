from collections import defaultdict
for _ in range(int(input())):
    n,q = list(map(int, input().split()))
    a = list(map(int, input().split()))

    b = sorted(a)
    idx = defaultdict(list)
    for i in range(n):
        idx[a[i]].append(i)

    ans = 0

    for i in range(n-1, -1, -1):
        tar = idx[b[i]].pop()
        if i == tar: continue

        diff = tar^i
        crit_bit = 1 << (diff.bit_length()-1)

        ans = max(ans, crit_bit)
    
    print(ans)