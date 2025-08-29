for i in range(int(input())):
    n = int(input())
    a = input().lower()
    b = list(set(a))

    if len(b) == 4 and 'o' in b and 'm' in b and 'e' in b and 'w' in b:
        check = 0
        boo = True
        for i in range(n):
            if a[i] == 'm':
                if check != 0:
                    boo = False
                    break
                elif a[i+1] == 'e':
                    check += 1
            elif a[i] == 'e':
                if check != 1:
                    boo = False
                    break
                elif a[i+1] == 'o':
                    check += 1
            if a[i] == 'o':
                if check != 2:
                    boo = False
                    break
                elif a[i+1] == 'w':
                    check += 1
            if a[i] == 'w':
                if check != 3:
                    boo = False
                    break

        print('YES' if boo else 'NO')
    else:
        print('NO')
    