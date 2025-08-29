for i in range(int(input())):
    n = int(input())

    count = 0
    final = []
    while n > 9-count:
        final.append(9-count)
        n-= 9-count
        count += 1
    
    if n != 0: final.append(n)
    print(*final[::-1], sep='')
    print()