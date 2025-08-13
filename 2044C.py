for i in range(int(input())):
    m,a,b,c = list(map(int, input().split()))

    count = 0
    if a > m:
        count += m
        rem1 = 0
    else:
        count += a
        rem1 = m-a
    if b > m: 
        count += m
        rem2 = 0
    else:
        count += b
        rem2 = m-b

    if c >= rem1 + rem2:
        count += rem1+rem2
    else:
        count += c

    print(count)