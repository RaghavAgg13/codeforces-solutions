for i in range(int(input())):
    a,s = input().split()
    
    a = '0'*(len(s)-len(a))+a

    b = []
    check = True
    l1,l2 = len(a)-1, len(s)-1
    while l1 > -1 and l2 > -1:

        if a[l1] > s[l2]:
            if l2 == 0:
                check = False
                break
            num = int(s[l2-1:l2+1]) - int(a[l1])
            l2 -= 2
        else:
            num = int(s[l2]) - int(a[l1])
            l2 -= 1
        l1 -= 1

        if not 0 <= num <= 9:
            check = False
            break
        b.append(str(num))

    if list(set(a[:l1+1])) != [] and list(set(a[:l1+1])) != ['0']:
        check = False

    if check:
        print(int(''.join(b[::-1])))
    else: print(-1)