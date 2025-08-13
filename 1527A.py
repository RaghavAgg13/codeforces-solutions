for i in range(int(input())):
    n = int(input())

    if n&(n-1) == 0:
        print(n-1)
    else:
        highest = n
        highest |= highest >> 1
        highest |= highest >> 2
        highest |= highest >> 4
        highest |= highest >> 8
        highest |= highest >> 16
        print(highest//2)