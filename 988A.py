n,k = list(map(int, input().split()))
a = list(map(int, input().split()))

b = list(set(a))[:k]
if len(b) >= k:
    print('YES')
    for i in b:
        print(a.index(i)+1, end=' ')
    print()

else:
    print('NO')