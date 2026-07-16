for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    even, odd = {0: 1}, {}
    ways = 1
    MOD = 1000000007

    for i in range(n):
        if a[i] == -1:
            even[0], odd[-1] = (even[0] + odd.get(-1, 0))%MOD, (even[0] + odd.get(-1, 0))%MOD
            ways = even[0]
        elif a[i] > 0:
            odd[a[i]], even[0] = (odd.get(a[i], 0) + even[0])%MOD, (even[0] + odd.get(a[i], 0))%MOD
            
            odd[0], even[-a[i]], even[-1-a[i]], odd[-1], ways = (
                    (odd.get(0, 0) + even.get(-a[i], 0))%MOD,
                    (even.get(-a[i], 0) + odd.get(0, 0))%MOD,
                    (even.get(-1-a[i], 0) + odd.get(-1, 0))%MOD,
                    (odd.get(-1, 0) + even.get(-a[i]-1, 0))%MOD,
                    (even[0] + odd.get(0, 0) + even.get(-a[i], 0))%MOD
                )
    
    print(ways)