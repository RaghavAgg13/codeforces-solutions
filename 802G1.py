a = input()
n = len(a)
b = ""
for i in range(n):
    if a[i] in ['h', 'e', 'i', 'd']:
        b += a[i]
a = b
n = len(a)
c = a[0]
for i in range(1, n):
    if a[i] != a[i-1]: c += b[i]
a = c
n = len(a)

def solve():
    for i in range(n):
        if a[i] != 'h': continue
        for j in range(i+1, n):
            if a[j] != 'e': continue
            for k in range(j+1, n):
                if a[k] != 'i': continue
                for m in range(k+1, n):
                    if a[m] != 'd': continue
                    for b in range(m+1, n):
                        if a[b] != 'i': continue
                        return "YES"
    return "NO"
                    

print(solve())  