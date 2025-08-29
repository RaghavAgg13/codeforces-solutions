for i in range(int(input())):
    n = int(input())
    if n > 45:
        print(-1)
    else:
        count = 0
        a = []
        while n > 9-count:
            a.append(9-count)
            n-=9-count
            count += 1
        if n != 0 and n not in a:
            a.append(n)
            print(*a[::-1], sep="")
        else:
            print(-1)