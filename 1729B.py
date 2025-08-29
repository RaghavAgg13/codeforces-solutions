for i in range(int(input())):
    n = int(input())
    a = input()

    i = 0
    while i < n:
        b = int(a[i])
        if b > 2:
            print(chr(96+b), end='')
        elif i <= n-3 and a[i+2] == '0':  
            if i <= n-4 and a[i+3] == '0':
                print(chr(96+b), end='')
            else: 
                print(chr(96 + int(a[i:i+2])), end='')
                i += 2
        else: 
            print(chr(96+b), end='')
        i += 1

    print()