from collections import Counter
for i in range(int(input())):
    n = list(map(int, input().split()))
    a = list(map(int, input().split()))

    count = Counter(a)

    s = sum([val//2 for index,val in count.items()])
    print(s)