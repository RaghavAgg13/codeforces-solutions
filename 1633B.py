for i in range(int(input())):
    a = input()
    if a.count("0") != a.count("1"): ans = min(a.count("0") , a.count("1"))
    else: ans = a.count("0")-1
    print(ans)