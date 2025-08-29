for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    count = 0
    final = 0
    for i in range(n):
        if a[i] == 0:
            count += 1
        else:
            if count >= k:
                final += count//(k+1)
                if count%(k+1) == k: final += 1
            count = 0

    if count >= k:
        final += count//(k+1)
        if count%(k+1) == k: final += 1

    print(final)