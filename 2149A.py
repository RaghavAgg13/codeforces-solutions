for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    odds = 0
    for i in a:
        if i == -1: odds += 1
        elif i == 0: count += 1
    
    print(count+2 if odds%2 else count)