for j in range(int(input())):
    n,a,b = list(map(int, input().split()))

    g = min(n,b)
    solns = [0, g]
    if 0 <= (b-a) <= g: solns.append(b-a)
    if 0 <= (b-a+1) <= g: solns.append(b-a+1)
    
    final = n*a
    for i in solns:
        final = max(final, (n-i)*a+i*(2*b-i+1)//2)
    print(int(final))