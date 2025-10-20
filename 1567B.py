for i in range(int(input())):
    a,b = list(map(int, input().split()))

    ans = a
    cur_xor = 0
    for i in range(4*(a//4), a): cur_xor ^= i

    if cur_xor != b: ans += 1 if cur_xor^b != a else 2
    print(ans)  