import math
for i in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))

    if 0 in s:
        s.remove(0)
        print(math.prod(s))
    elif len(list(set(s))) == 1:
        print(math.prod(s[:-1])*(s[-1]+1))
    else:
        min_val =  min(s)
        s.remove(min_val)
        print(math.prod(s)*(min_val+1))