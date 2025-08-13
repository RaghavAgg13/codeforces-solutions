n = int(input())

if n%2 == 1:
    print('-1')
else:
    for i in range(n):
        print(n-i, end=' ')