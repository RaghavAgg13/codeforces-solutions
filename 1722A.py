t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    b = False

    if n == 5:
        for i in ['T', 'i', 'm', 'u', 'r']:
            if i in s:
                b = True
            else: 
                b = False
                break

    print('YES' if b else 'NO')