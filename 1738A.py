for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    frost = sorted([b[i] for i in range(n) if a[i] == 0])
    fire = sorted([b[i] for i in range(n) if a[i] == 1])

    if len(frost) == len(fire):
        print(sum(b)*2-min(b))
    elif len(frost) > len(fire):
        print(sum(b)*2-sum(frost[:len(frost)-len(fire)]))
    else:
        print(sum(b)*2-sum(fire[:len(fire)-len(frost)]))

    