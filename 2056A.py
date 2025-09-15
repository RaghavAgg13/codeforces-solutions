for i in range(int(input())):
    n,m = list(map(int, input().split()))

    perimeter = 4*m
    a,b = list(map(int, input().split()))
    for i in range(n-1):
        a,b = list(map(int, input().split()))
        perimeter += (a+b)*2

    print(perimeter)