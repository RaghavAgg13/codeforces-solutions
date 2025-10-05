for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    left,right = 0,n-1
    pos,check = 1,0

    while left < right:
        if a[left] == pos: left += 1
        elif a[right] == pos: right -= 1
        else: 
            check = 1
            break
        pos += 1
        
    print('NO' if check else 'YES')