from collections import Counter
for i in range(int(input())):
    n,k = list(map(int, input().split()))
    s = sorted(list(input()))
    a = dict(Counter(s))
    
    counto = []
    counte = []
    for key, val in a.items():
        if val%2 == 1: 
            counto.append(val)
        else:
            counte.append(val)

    odd = sum(counto)
    even = sum(counte)
    
    