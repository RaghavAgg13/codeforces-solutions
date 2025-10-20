for i in range(int(input())):
    n = int(input())
    s = input()
    a = ''.join(sorted(s))

    cnt = 0
    ans = []
    for i in range(n):
        if a[i] != s[i]:
            cnt += 1
            ans.append(i+1)

    if cnt:
        print(1)
        print(cnt, *ans)
    else:
        print(0)