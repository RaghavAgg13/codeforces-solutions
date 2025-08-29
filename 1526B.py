for i in range(int(input())):
    n = int(input())

    a = n%11
    
    print('YES' if not n//11 < 10*a else 'NO')