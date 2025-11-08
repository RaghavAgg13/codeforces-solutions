for i in range(int(input())):
    x,y = list(map(int, input().split()))

    if x >= y:
        print('YES')
    elif x == 2 and y == 3: print("YES")
    elif x in [1,2,3]: print("NO")
    else: print('YES')