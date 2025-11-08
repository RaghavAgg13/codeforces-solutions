for i in range(int(input())):
    a = input()
    b = input()
    
    for i in set(a):
        if i in b:
            print('YES')
            break
    else:
        print('NO')