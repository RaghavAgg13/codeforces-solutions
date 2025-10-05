for i in range(int(input())):
    a,b,x,y = list(map(int, input().split()))

    total_moves = b-a

    if total_moves < 0:
        print(y if a-b == 1 and a%2 else -1)
    else:
        if x > y:
            count = total_moves//2*y+total_moves//2*x
            if a%2:
                if total_moves%2: count += x
            else:
                if total_moves%2: count += y
            print(count)
        else: print( total_moves*x)