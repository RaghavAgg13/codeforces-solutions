for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    avg = sum(a)//n
    fail = False

    carry = 0
    for i in a:
        if i > avg:
            carry += i-avg
        else: carry -= avg-i
        if carry < 0:
            fail = True
            break

    if fail or carry < 0:
        print('NO')
    else:
        print('YES')