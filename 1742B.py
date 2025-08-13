for i in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    if len(list(set(s))) == len(s):
        print('YES')
    else: print('NO')