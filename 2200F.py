for i in range(int(input())):
    n,m = list(map(int, input().split()))

    pa, shop = [], []
    for i in range(n):
        a = list(map(int, input().split()))

        pa.append(a)
    
    for i in range(m):
        a = list(map(int, input().split()))

        shop.append(a)
    
    print(pa, shop)