for _ in range(int(input())):
    x,y = list(map(int, input().split()))

    if x < y:
        print("NO")
        continue

    if x%y:
        print("NO")
    else:
        print("YES")