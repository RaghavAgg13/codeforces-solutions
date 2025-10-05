for i in range(int(input())):
    n = int(input())
    a = input()

    check = 0
    if 'L' not in a or 'R' not in a:
        print(-1)
    else:
        for i in range(n-1):
            if a[i] == 'R':
                for j in range(i+1, n):
                    if a[j] == 'L':
                        check = 1
                        print(0)
                        break
        
            if a[i] == 'L' and a[i+1] == 'R':
                check = 1
                print(i+1)
                break

            if check: break

        if not check: print('-1')