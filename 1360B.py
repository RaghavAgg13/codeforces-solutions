for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse=True)

    val = max(l) - min(l)

    for i in range(1, n):
        alpha = abs(l[i] - l[i-1])
        if alpha <= val:
            val = alpha

    print(val)