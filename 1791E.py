for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    positive_min = 1000000000
    negative_max = -1000000000
    s = 0
    count = 0

    for i in a:
        if i <= 0:
            s -= i
            count += 1
            negative_max = max(negative_max, i)
        else: 
            positive_min = min(positive_min, i)
            s += i


    if count%2:
        s += negative_max
        s += max(-negative_max-positive_min*2, negative_max)
    print(s)    