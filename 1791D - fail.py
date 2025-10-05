for i in range(int(input())):
    n = int(input())
    a = list(input())

    total = len(set(a))
    count = 0
    check = 1
    prev = set()
    for i in range(n):
        if a[i] not in prev:
            prev.add(a[i])
            count += 1
        else:
            print(count+len(set(a[i:])))
            check = 0
            break
    if check: print(count)