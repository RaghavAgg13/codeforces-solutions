a,b,s = list(map(int, input().split()))

dist = abs(a)+abs(b)
if dist%2 == s%2 and dist <= s: print('Yes')
else: print('No')