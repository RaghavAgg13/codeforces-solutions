for i in range(int(input())):
    a = input()
    a = a[::-1]

    count = len(a)-1

    parts = ['00', '25', '50', '75']
    for part in parts:
        if part[1] in a:
            idx1 = a.index(part[1])
            if part[0] in a[idx1+1:]:
                idx2 = a[idx1+1:].index(part[0])
                count = min(count, idx1+idx2)
    print(count)