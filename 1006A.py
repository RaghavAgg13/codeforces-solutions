n = int(input())
a = list(map(int, input().split()))

for i in a:
    if i%2: print(i, end=' ')
    else: print(i-1, end=' ')
print()