for _ in range(int(input())):
    n,a,q = list(map(int, input().split()))
    st = input()

    chk = 0
    addn = a
    if (a == n):
        print("YES")
        continue
    
    for i in st:
        if i == "+": 
            a += 1
            addn += 1
        else: a -= 1
        
        if a == n:
            chk = 1
            break

    if (chk):
        print("YES")
    elif addn >= n:
        print("MAYBE")
    else:
        print("NO")