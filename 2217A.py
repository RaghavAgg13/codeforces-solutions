for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    s = sum(a)

    if (s%2 or (k*n)%2 == 0):
        print("YES")
    else:
        print("NO")
