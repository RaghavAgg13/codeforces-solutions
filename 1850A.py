t = int(input())

for i in range(t):
    a,b,c = sorted(list(map(int, input().split(' '))))
    print('YES' if b + c >=10 else 'NO')