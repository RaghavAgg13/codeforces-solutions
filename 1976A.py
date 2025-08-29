for i in range(int(input())):
    n = int(input())
    a = input()
    d = ''
    e = ''

    check = 1
    if a.lower() == a:
        for i in range(n):
            if  96 <= ord(a[i]) <= 122:
                d += a[i]
            elif 48 <= ord(a[i]) <= 57:
                e += a[i]
            else:
                check = 0
                break
        
        if d == "".join(sorted(d)) and e == "".join(sorted(e)):
            if a != e+d: check = 0 
        else: check = 0
    else: check = 0

    print('YES' if check else 'NO')