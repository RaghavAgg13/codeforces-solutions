from collections import Counter
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a = [abs(i) for i in a]

    b = Counter(a)
    count = 0
    for x,i in b.items():
        if x == 0:
            count += 1
        elif i <= 2:
            count += i
        else:
            count += 2
    
    print(count)