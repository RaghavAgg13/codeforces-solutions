import math
for i in range(int(input())):
    s = list(map(int, input().split()))
    l1, l2, l3 = s[0::2]
    b1, b2, b3 = s[1::2]
    b = False

    # print(l1, l2, l3, b1, b2, b3)
    if int(math.sqrt(l1*b1 + l2*b2 + l3*b3)) == math.sqrt(l1*b1 + l2*b2 + l3*b3):
        if (l1 == l2 == l3 == (b1+b2+b3)) or (b1 == b2 == b3 == (l1+l2+l3)):
            b = True
        elif (l2 == l3 and b1 == b2+b3 and l1+l2 == b1) or (b2 == b3 and l1 == l2+l3 and b1+b2 == l1):
            b = True

    print('YES' if b else 'NO')