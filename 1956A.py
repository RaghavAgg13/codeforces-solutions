for i in range(int(input())):
    k,q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    n = list(map(int, input().split()))


    for i in n:
        print(min(min(a)-1, i), end=' ')
    print()