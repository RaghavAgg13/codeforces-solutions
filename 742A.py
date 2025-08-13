n = int(input())

if n == 0: print('1')
else:
    n = n%4
    if n%4 == 0:
        print('6')
    elif n%2 == 0:
        print('4')
    elif n%3 == 0:
        print('2')
    else: print('8')