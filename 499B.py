n,m = list(map(int, input().split()))
words1 = []
words2 = []
for i in range(m):
    w1, w2 = list(map(str, input().split()))
    words1.append(w1)
    words2.append(w2)

ws = list(map(str, input().split()))

for i in range(n):
    if ws[i] in words1:
        w1 = words1[words1.index(ws[i])]
        w2 = words2[words1.index(w1)]
    else:
        w1 = words2[words2.index(ws[i])]
        w2 = words1[words2.index(w1)]
    
    n1, n2 = len(w1), len(w2)
    print(w2 if n1>n2 else w1, end=' ')