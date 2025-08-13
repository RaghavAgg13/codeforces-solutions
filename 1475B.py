for i in range(int(input())):
    n = int(input())
    b = False

    if n >= 2020:
        if n%2020 == 0 or n%2021 == 0:
            b = True
        else:
            for i in range(1, n//2020+1):
                if (n-i*2020)%2021 == 0:
                    b = True
                    break

    print('YES' if b else 'NO')