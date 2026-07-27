from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    st = []
    cnt = 1
    for i in range(1, n):
        if a[i] == a[i-1]: cnt += 1
        else:
            st.append(cnt)
            cnt = 1
    
    st.append(cnt)

    ways = 0
    prev_dec = 10**9

    while n > 0:
        new_st = []

        dec = 0
        for i in range(len(st)):
            if st[i]: 
                dec += 1
                st[i] -= 1
                if st[i] > 0: new_st.append(st[i])
        
        if k == n: ways += 1

        if dec < prev_dec and k > n and (k-n)%dec == 0: ways += 1

        n -= dec
        prev_dec = dec

        st = new_st
    
    print(ways)