n = int(input())
a = sorted(list(map(int, input().split())))
b = False

if len(list(set(a))) == 2 and a.count(max(a)) != 1:
    b = True
elif len(a) == 2 and max(a)>min(a)*2:
    b = False
else:
    for i in range(n-2):
        if b: break
        k = i + 2
        for j in range(i+1, n-1):
            while k < n and a[i] + a[j] > a[k]:
                k += 1
            if k - 1 > j:
                b = True
                break
    

print('YES' if b else 'NO')