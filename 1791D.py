
for i in range(int(input())):
    n = int(input())
    a = input()
 
    prefix = set()
    suffix = set()
    p,s = [0], [0]
 
    for i in range(n):
        if a[i] not in prefix:
            prefix.add(a[i])
            p.append(p[-1]+1)
        else:
            p.append(p[-1])
    
    for i in range(n-1, -1, -1):
        if a[i] not in suffix:
            suffix.add(a[i])
            s.append(s[-1]+1)
        else: s.append(s[-1])
 
    p.remove(p[0])
    s.remove(s[0])
    
    s.reverse()
 
    cnt = 0
    for i in range(n-1):
        cnt = max(cnt, p[i]+s[i+1])
    print(cnt)