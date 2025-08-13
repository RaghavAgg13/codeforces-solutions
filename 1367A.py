t = int(input())

for i in range(t):
    b = input()

    print(b[0:2], end='')
    for i in range(2, len(b)-1, 2):
        print(b[i+1], end='')
    print()