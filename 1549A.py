for i in range(int(input())):
    n = int(input())


    check = False
    for i in range(2, n):
        rem = n%i
        if n//i != i:
            print(i,n//i)
            check = True
            break
        else:
            for j in range(i+1, n+1):
                if n%j == rem:
                    print(i, j)
                    check = True
                    break

        if check: break