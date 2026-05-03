for i in range(int(input())):
    n = int(input())
    a = input()

    if (a.count(')') != a.count("(")):
        print("NO")
    else:
        print("YES")