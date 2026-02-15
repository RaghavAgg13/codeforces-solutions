import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, ax, ay, bx, by = list(map(int, input().split()))
    
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    coords = [[ax, ay]]
    for i in range(n):
        coords.append([x[i], y[i]])

    coords.sort()
    
    coords.append([bx, by])
    coords.append([bx+1, by]) 

    prev_x = ax
    
    time_lo, time_hi = 0, 0
    last_lo, last_hi = ay, ay
    
    y_hi, y_lo = ay, ay
    
    for x, y in coords:
        if x != prev_x:
            span = y_hi-y_lo
            h_move = x-prev_x
            
            opt1 = time_lo+abs(last_lo-y_lo)+span
            opt2 = time_hi+abs(last_hi-y_lo)+span
            
            new_time_hi = min(opt1, opt2)+h_move
            
            opt3 = time_lo+abs(last_lo-y_hi)+span
            opt4 = time_hi+abs(last_hi-y_hi)+span
            
            new_time_lo = min(opt3, opt4)+h_move
            
            time_hi = new_time_hi
            time_lo = new_time_lo
            
            last_hi = y_hi
            last_lo = y_lo
            prev_x = x
            
            y_hi, y_lo = y, y
        else:
            y_hi = max(y_hi, y)
            y_lo = min(y_lo, y)

    print(min(time_lo, time_hi)-1)