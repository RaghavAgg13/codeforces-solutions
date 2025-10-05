from collections import Counter

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = Counter(a)
    count = sum([freq//3 for num,freq in b.items()])
    print(count)        