import math

for i in range(int(input())):
    k = int(input())

    d = math.ceil(math.sqrt(k))
    turning_point = d**2 - d + 1

    if k >= turning_point:
        r = d
        c = d**2 - k + 1
    else:
        c = d
        prev_sq_max = (d - 1)**2
        r = k - prev_sq_max
    
    print(r, c)