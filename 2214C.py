for i in range(int(input())):
    a,b,c = list(map(int, input().split()))
    s = (a+b+c)
    print((s%3)^((s-s%3)//3))