for i in range(int(input())):
    n = int(input())

    count = 1
    while n >= 4:
        n //= 4
        count *= 2
    
    print(count)