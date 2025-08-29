for i in range(int(input())):
    a = list(sorted(list(map(int, input().split())), reverse=True))
    s_all = max(a)
    a1 = a[-1]
    a2 = a[-2]
    a3 = s_all-a1-a2

    print(a1,a2,a3)