t = int(input())
for i in range (t):
    count = 0
    a,b,c,d = map(int, input().split())
    for j in [b,c,d]:
        if a < j:
            count += 1
    print(count)    