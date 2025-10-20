for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    check = True
    carry = 0
    for i in range(n):
        if a[i]+carry >= i:
            carry += a[i]-i
        else:
            check = False
            break
    
    print('YES' if check else 'NO')