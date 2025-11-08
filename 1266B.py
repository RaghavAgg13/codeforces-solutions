n = int(input())
a = list(map(int, input().split()))

for i in a:
    if i >= 15 and not ((i//7)*7)%2 and  1 <= i%7 <= 6:
        print('YES')
    else:
        print('NO')