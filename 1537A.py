for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if sum(a)/n > 1:
        print(abs(sum(a)-n))
    elif sum(a)/n == 1.0:
        print(0)
    else:
        print(1)