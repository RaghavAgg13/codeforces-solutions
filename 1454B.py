from collections import Counter
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = Counter(a)
    b = [num for num, value in counts.items() if value == 1]

    if b != []:
        print(a.index(min(b))+1)
    else:
        print(-1)