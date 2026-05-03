for i in range(int(input())):
    a,b = list(map(int, input().split()))

    if (a%2 + b%2 == 2):
        print("NO")
    else:
        print("YES")