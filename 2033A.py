for i in range(int(input())):
    n = int(input())
    pos = 0
    b = True
    i = 1
    while -n <= pos <= n:
        b = not b
        pos += ((-1)**i)*(2*i-1)

    print('Kosuke' if b else 'Sakurako')