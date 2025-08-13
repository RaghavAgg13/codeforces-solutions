for i in range(int(input())):
    a, b, c, k = map(int, input().split())
    a,b,c = list(sorted([a,b,c]))
    limit = c
    triplets = []

    for x in range(1, c + 1):
        if k % x != 0:
            continue
        for y in range(x, c + 1):
            if (k // x) % y != 0:
                continue
            z = k // (x * y)
            if z >= y and z <= c:
                triplets.append((x, y, z))

    final = 0
    if triplets != []:
        for set in triplets:
            if a >= set[0] and b >= set[1] and c >= set[2]:
                final = max(final, (a-set[0]+1)*(b-set[1]+1)*(c-set[2]+1))
    print(final)