for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = sum([a[i]- b[i] for i in range(n) if a[i] > b[i]])
    c += 1 

    print(c)