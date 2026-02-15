from collections import Counter
for i in range(int(input())):
    n = int(input())
    a = []

    for i in range(n): a.append(input())
    
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (a[i][0] == a[j][0])^(a[i][1] == a[j][1]):
                cnt += 1
    
    print(cnt)