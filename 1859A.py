for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    split = []
    for i in l:
        if i != 1:
            split = [[i]]
            l.remove(i)
            break

    count1 = l.count(1)
    for i in range(n-1):
        a = l[0]
        l.remove(l[0])
        b = False
        if a != 1:
            for spl in split:
                if a%spl[0] == 0:
                    spl.append(a)
                    b = True
                    break
            if not b:
                split.append([a])

    print(split)
    b = [1*count1]
    c = []
    for i in split:
        if len(split) > 1:
            c += i
        else:
            b.append(i[0])

    print(b)
    print(c)
