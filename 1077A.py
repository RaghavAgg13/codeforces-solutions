for i in range(int(input())):
    a,b,k = list(map(int, input().split()))

    f = (a-b)*(k//2) + a*bool(k%2)
    print(f)