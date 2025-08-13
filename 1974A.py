for i in range(int(input())):
    x,y = list(map(int, input().split()))
 
    nos = y//2 + bool(y%2)
 
    if y == 0:
        print(x//15 + bool(x%15))
        continue
    elif x == 0:
        print(y//2 + bool(y%2))
        continue
 
    delta = 7*(y//2)
    rem = (x-delta)
    if y%2==0 and delta < x:
            nos += rem//15 + bool(rem%15)
    elif y%2==1:
        if delta +11 < x:
            rem -= 11
            nos += rem//15 + bool(rem%15)
    
    print(nos)