for i in range(int(input())):
    l1,l2,l3 = list(map(int, input().split()))

    if (l1 == l2 and not l3%2 and l3 !=1) or (l2 == l3 and not l1%2 and l1!=1) or (l3 == l1 and not l2%2 and l2!=1) or (l1+l2==l3) or (l2+l3==l1) or (l3+l1==l2):
        print('YES')
    else:
        print('NO')