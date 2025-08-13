t = int(input())

for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    solns = [0]

    for i in s:
        if i == 0:
            count += 1
        else:
            solns.append(count)
            count = 0

    if count != 0: solns.append(count)

    print(max(solns))