import math
y,w = sorted(list(map(int, input().split())))

if w != 6:
    poss = 7-w
    print(int(poss/math.gcd(poss, 6)),'/', int(6/math.gcd(poss, 6)), sep='')
else:
    print('1/6')