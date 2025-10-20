for i in range(int(input())):
    n,a,b = list(map(int, input().split()))
    s = input()

    while '00' in s: s = s.replace('00', '0', -1)
    while '11' in s: s = s.replace('11', '1', -1)
    switch = min(s.count('0'), s.count('1'))+1

    if b >= 0:
        print((a+b)*n)
    else:
        print(a*n+b*switch)