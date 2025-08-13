t = int(input())

for i in range(t):
    j = 0
    n = int(input())
    s = list(map(int, input().split(' ')))
    sorted = list(dict.fromkeys(s))
    
    for i in sorted:
        if s.count(i) == 1: 
            j = s.index(i)
    print(j+1)