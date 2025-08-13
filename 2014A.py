for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    gold = 0
    helped = 0

    for i in range(n):
        if a[i] >= k:
            gold += a[i]
        elif a[i] == 0 and gold > 0:
            gold -=1
            helped += 1

    print(helped)