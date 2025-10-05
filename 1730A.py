from collections import defaultdict
for i in range(int(input())):
    n,c = list(map(int, input().split()))
    a = list(map(int, input().split()))

    b = defaultdict(int)
    for i in a:
        b[i] += 1

    cost = 0
    for key,value in b.items():
        if c < value:
            cost += c
        else:
            cost += value

    print(cost)