for i in range(int(input())):
    n = int(input())

    b = False
    for i in range(1, int(n**(1/3))+1):
        delta = n-i**3
        if round((delta)**(1/3))**3 == delta and delta != 0:
            b = True
            break

    print('YES' if b else 'NO')