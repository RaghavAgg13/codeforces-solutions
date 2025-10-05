from math import ceil
for i in range(int(input())):
    n,h = list(map(int, input().split()))
    a = list(map(int, input().split()))

    m1 = max(a)
    a.remove(max(a))
    m2 = max(a)

    count = h//(m1+m2)*2
    h %= m1+m2
    if h > m1: count += 2
    elif h > 0: count += 1
    print(count)