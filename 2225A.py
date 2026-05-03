for i in range(int(input())):
    x,y = list(map(int, input().split()))

    k = y//x
    if (k > 2):
        print("YES")
    else:
        print("NO")
