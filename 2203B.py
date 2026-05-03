for _ in range(int(input())):
    n = str(input())
    
    l = len(n)
    changes = []

    cur_sum = 0
    for i in range(0, l):
        cur_sum += int(n[i])
        if i == 0:
            if int(n[i]) > 1: changes.append(int(n[i])-1)
        else:
            changes.append(int(n[i]))
    

    changes = sorted(changes, reverse=True)

    cnt = 0
    while cur_sum > 9 and cnt < len(changes):
        cur_sum -= changes[cnt]
        cnt += 1
    
    print(cnt)