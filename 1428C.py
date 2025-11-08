for i in range(int(input())):
    a = input()
    cnt = 0
    for i in a:
        if i == 'B' and cnt != 0: cnt -= 1
        else: cnt += 1
    
    print(cnt)