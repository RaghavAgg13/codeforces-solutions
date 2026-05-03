for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    for i in a:
        if i == 1: cnt += 1
        else: break

    if cnt == n:
        if (n%2): print("First")
        else: print("Second")
    else:
        if (cnt%2): print("Second")
        else: print("First")