import bisect
n = int(input())
x = sorted(list(map(int, input().split(' '))))

q = int(input())

for i in range(q):
    count = 0
    qi = int(input())
    print(bisect.bisect_right(x, qi))