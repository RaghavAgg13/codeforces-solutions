for i in range(int(input())):
    n = int(input())

    m_ = 1
    m = 10e9
    rem = []
    for i in range(n):
        a,x = list(map(int, input().split()))
        if a == 1: m_ = max(m_, x)
        elif a == 2: m = min(m, x)
        else: rem.append(x)

    rem = {val for val in rem if m_ <= val <= m}
    result = (m - m_ + 1) - len(rem)
    
    print(result if result > 0 else 0)