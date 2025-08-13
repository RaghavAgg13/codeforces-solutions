for i in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))

    if (s.count(1)%2 == s.count(2)%2 == 0 and s.count(1) != 1 and s.count(2) != 1) or ((s.count(1) - s.count(2)*2)%2 == 0 and s.count(1) != 0):
        print('YES')
    else:
        print('NO')