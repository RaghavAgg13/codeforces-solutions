for i in range(int(input())):
    x,k = list(map(int, input().split()))

    pos = 0
    jumps = []
    while pos != x:
        val = x-pos if (x-pos)%k != 0 else x-1-pos

        jumps.append(str(val))
        pos += val

    print(len(jumps))
    print(' '.join(jumps))