for _ in range(int(input())):
    n = int(input())
    b = []
    for i in range(n):
        x = list(map(int, input().split()))[1:]
        b.append(list(dict.fromkeys(x[::-1])))

    s = set()
    a = []

    # print(b)

    for _ in range(n):
        u = None
        idx = -1
        for i in range(len(b)):
            cur = [k for k in b[i] if k not in s]
            if u is None or cur < u:
                u = cur
                idx = i
        
        a.extend(u)
        s.update(u)
        b.pop(idx)

    print(*a)