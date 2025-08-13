import math
for i in range(int(input())):
    n, x = list(map(int, input().split()))
    if n <= 2:
        print('1')
    else:
        print(math.ceil((n-2)/x)+1)