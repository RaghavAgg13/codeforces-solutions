for i in range(int(input())):
    l,r,k = list(map(int, input().split()))

    odd = (r+1)//2-l//2
    print('YES' if odd <= k or l == r != 1 else 'NO')