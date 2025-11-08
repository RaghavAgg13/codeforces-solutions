for i in range(int(input())):
    a = input()

    if len(a)%2:
        print("NO")
    else:
        if a[0] == ')' or a[-1] == "(":
            print('NO')
        else:
            print('YES')