for i in range(int(input())):
    x,y = list(map(int, input().split()))

    print(x+y+(abs(abs(x-y)-1)) if x != y else x+y)