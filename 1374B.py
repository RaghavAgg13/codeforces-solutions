t = int(input())

for i in range(t):
    count = 0
    b = 0
    n = int(input())

    if n != 1:
        while n%6 == 0:
            n /= 6
            count += 1
        while n%3 == 0:
            n /= 3
            count += 2
        
        if  n != 1: count = -1

    print(count)