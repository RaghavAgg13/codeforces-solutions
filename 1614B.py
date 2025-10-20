for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a = sorted(enumerate(a), key=lambda item: item[1], reverse=True)

    pos = [0]*n
    dist = 0
    idx, counter = 1, 0
    for i in a:
        index, val = list(i)
        pos[index] = idx*((-1)**counter)
        dist += 2*val*idx
    
        counter += 1
        if 1-counter%2: idx += 1

    print(dist)
    print(0, *pos)