for i in range(int(input())):
    c,sum = list(map(int, input().split()))
    
    s = (c-sum%c)*(sum//c)**2 + (sum%c)*(sum//c + bool(sum%c))**2
    print(s)