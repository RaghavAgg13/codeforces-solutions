n,h,a,b,k = list(map(int, input().split()))

for i in range(k):
    ta,fa,tb,fb = list(map(int, input().split()))

    if ta == tb: 
        print(abs(fa-fb))
        continue

    ans = abs(ta-tb)
    if fa < a:
        ans += a-fa
        fa = a
    elif fa > b:
        ans += fa-b
        fa = b
    if fb < a:
        ans += a-fb
        fb = a
    elif fb > b:
        ans += fb-b
        fb = b
    
    ans += abs(fa-fb)

    print(ans)