for i in range(int(input())):
    x,y = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    arr = []
    if x < y:
        for i in a:
            if i in b:
                arr.append(i)
                break
    else:
        for i in b:
            if i in a:
                arr.append(i)
                break
    
    length = len(arr)
    if length:
        print("YES")
        print(length, *arr)
    else: print('NO')