for i in range(int(input())):
    n = int(input())

    k = n//3
    rem = n%3

    if rem == 1:
        print('12'*k+'1')
    elif rem == 2:
        print('21'*k+'2')
    else:
        print('21'*k)