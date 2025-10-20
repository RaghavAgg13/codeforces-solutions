for i in range(int(input())):
    n = int(input())

    while n > 33:
        if not n%33: 
            n = 0
            break
        
        while '33' in str(n):
            temp_str = str(n).replace('33', '')

            if temp_str == '': n = 0
            else: n = int(temp_str)
        n -= 33

    if n == 33 or n == 0:
        print('YES')
    else: print('NO')