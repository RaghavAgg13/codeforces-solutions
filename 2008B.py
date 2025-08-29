for i in range(int(input())):
    n = int(input())
    a = input()
    b = n**0.5


    if b == int(b):
        b = int(b)
        check = True
        if a[:b] == '1'*b and a[n-b:n] == '1'*b:
            for i in range(1, b-1):
                if a[b*i:b+b*i] != '1'+'0'*(b-2)+'1':
                    check = False
                    break
        else: check = False
    else: check = False


    print('Yes' if check else 'No')