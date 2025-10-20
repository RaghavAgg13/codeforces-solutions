from math import gcd
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    b = []
    for i in a:
        if i%2 == 0: count += 1
        else: b.append(i)
    
    a = b.copy()
    del b
    a.sort(reverse=True)

    final = n*count-(count*(count+1))//2
    n = len(a)
    for i in range(n):
        for j in range(i+1, n): 
            final += gcd(a[i],a[j])>1
    
    print(final)