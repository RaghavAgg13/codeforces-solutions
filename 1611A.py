for i in range(int(input())):
    n = int(input())

    if n%2 == 0:
        print(0)
    else:
        n = str(n)
        if '2' in n or '4' in n or '6' in n or '8' in n:
            if int(n[0])%2 == 0:
                print(1)
            else:
                print(2)
        else:
            print(-1)
