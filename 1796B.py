for i in range(int(input())):
    a = input()
    b = input()

    x = len(a)

    if a[0] == b[0]:
        print('YES')
        print(a[0]+"*")
        continue
    elif a[-1] == b[-1]:
        print('YES')
        print("*"+a[-1])
        continue

    for i in range(x-1):
        sub = a[i:i+2]
        if sub in b:
            print("YES")
            print('*' + sub + '*')
            break
    else:
        print('NO')