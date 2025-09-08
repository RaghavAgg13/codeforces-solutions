for i in range(int(input())):
    n1 = input()
    n2 = input()
    a = [n1[0], n1[1], n2[0], n2[1]]
    
    b = len(set(a))
    if b == 4:
        print(3)
    elif b == 3:
        print(2)
    elif b == 2:
        print(1)
    else:
        print(0)