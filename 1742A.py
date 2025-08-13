n = int(input())

for i in range(n):
    a,b,c, = sorted(list(map(int, input().split(' '))))

    print('YES' if c == a+b else 'NO')