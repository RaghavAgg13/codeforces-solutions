for _ in range(int(input())):
    n = int(input())
    a = list(input())

    cnt = 1
    chk = 0
    for i in range(1, n):
        if a[i] != a[i-1]:
            cnt += 1
        else:
            chk = 1
    
    cnt += chk
    if chk and (a[0] == a[-1]): cnt -= 1

    print(cnt)