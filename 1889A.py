t = int(input())
b = True
for i in range(t):
    count = 0
    n = int(input())
    if count < 10:
        if n%3 == 0:
            b = False
        else:
            b = True
    else:
        b = False
    count += 1

    print('First' if b else 'Second')