for i in range(int(input())):
    n,m = list(map(int, input().split()))
    a = input()
    b = input()

    a_g, b_g = 1,1
    t1,t2 = 0,0
    for i in range(1, n):
        if a[i] == a[i-1]:
            a_g = 0
        
            if a[i] == "1": t1 += 1
            else: t2 += 1
            
    
    for i in range(1, m):
        if b[i] == b[i-1]:
            b_g = 0
            break
    
    if a_g: 
        print("Yes")
    else:
        if b_g:
            if (t1 and t2):
                print("No")
            elif (t2 and (b[0] == b[-1] == "1")):
                print("Yes")
            elif (t1 and (b[0] == b[-1] == "0")):
                print("Yes")
            else:
                print("No")
        else:
            print("No")
