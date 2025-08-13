for i in range(int(input())):
    n = int(input())
    a = input()

    s = [3]
    for i in range(n):
        if a[i] == ">": s.append(s[-1]-1)
        else: s.append(max(s))

    print(max(s)-min(s)+1)