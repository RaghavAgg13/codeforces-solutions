for i in range(int(input())):
    ini = int(input())
    a = input()
    fin = int(input())
    b = input()
    key = input()

    for i in range(fin):
        if key[i] == 'V':
            a = b[i] + a 
        else:
            a += b[i]

    print(a)