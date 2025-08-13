from collections import defaultdict
for i in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    count = 0

    freq = defaultdict(int)
    for i in range(n):
        freq[s[i]-i] += 1

    # for j in range(n-1, 0, -1):
    #     for i in range(j-1, -1, -1):
    #         if s[j] - s[i] == j - i:
    #             count += 1
    
    print(freq)
    for i in freq.values():
        if i > 1:
            count += i*(i-1)//2

    print(count)