for i in range(int(input())):
    n = int(input())

    if n%2 == 0:
        print('YES')
        for i in range(n//2):
            print(chr(65+i%26)*2, end='', sep='')
        print()
    else: print('NO')