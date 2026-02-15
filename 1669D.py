for i in range(int(input())):
    n = int(input())
    a = input()

    while 'RR' in a: a = a.replace("RR", 'R', -1)
    while 'BB' in a: a = a.replace("BB", 'B', -1)
    while 'WW' in a: a = a.replace("WW", 'W', -1)

    n = len(a)
    if a[:2] == 'RW' or a[:2] == 'BW' or a[-2:] == 'WB' or a[-2:] == 'WR': check = False
    elif a in ['R', 'B']: check = False
    else: check = True
    for i in range(n-2):
        if a[i:i+3] in ['WBW', 'WRW']:
            check = False
            break
    
    # print(a)
    print("YES" if check else "NO")