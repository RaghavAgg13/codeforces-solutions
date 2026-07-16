from collections import defaultdict
for i in range(int(input())):
    n = int(input())

    arr = [0]*n

    # arr = [i for i in range(1, n+1)]
    # map = defaultdict(int)
    # rec = n+1

    # for i in range(1, n):
    #     if (map[arr[i]] == 1):
    #         map[arr[i]] -= 1
    #         map[arr[i]+arr[i-1]] -= 1
    #         if i+1 < n: map[arr[i]+arr[i+1]] -= 1
    #         arr[i] = rec
    #         map[arr[i]+arr[i-1]] += 1
    #         if i+1 < n: map[arr[i]+arr[i+1]] += 1
    #         rec += 1


    # print(*arr)

    arr = [n*2-i for i in range(n)]
    print(*arr)