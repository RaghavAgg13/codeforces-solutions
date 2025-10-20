for i in range(int(input())):
    a = input()
    n1,n2,n3 = a.count('A'), a.count('B'), a.count('C')

    if n1+n2==n3 or n2+n3==n1 or n3+n1==n2:
        if n1+n2==n3:
            a = a.replace('B', 'A', -1)
            a = a.replace('C', 'B', -1)
        elif n2+n3==n1:
            a = a.replace('C', 'B', -1)
        else:
            a = a.replace('C', 'A', -1)

        left = 1
        test = a[0]
        check = True
        for i in range(1, n1+n2+n3):
            if a[i] == test:
                left += 1
            else:
                if left > 0: left -= 1
                else: 
                    check = False
                    break
            
        print('YES' if check else 'NO')
    else:
        print('NO')