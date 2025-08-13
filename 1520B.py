import bisect

l = []
for i in range(1, 10):
    for j in range(1, 10):
        l.append(int(str(i)*j))
l.sort()

for i in range(int(input())):
    n = int(input())

    print(bisect.bisect_right(l, n))