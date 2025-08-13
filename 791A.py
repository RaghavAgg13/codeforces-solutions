a,b= list(map(int, input().split(" ")))
l = 0
while True:
    if a <= b:
        a *=3
        b *=2
        l +=1
    else:
        print(l)
        break