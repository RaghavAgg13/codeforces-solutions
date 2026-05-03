def chain_sum(s):
    s_ = 0
    cur = s
    while (cur > 9):
        s__ = 0

        while (cur > 9):
            s__ += cur%10
            cur //= 10

        if (cur > 0): s__ += cur%10

        s_ += s__
        cur = s__
    s_ += cur
    return s_

for _ in range(int(input())):
    a = input()

    freq = [0]*10
    T = 0
    for i in a:
        freq[int(i)] += 1
        T += int(i)
    
    for i in range(1, 9*len(a)+1):
        s = chain_sum(i)
        if T != s and T != s + i: continue

        temp_freq = freq[:]
        st = str(i)
        cur = i
        while (cur > 9):
            sum = 0
            while (cur > 9):
                temp_freq[cur%10] -= 1
                sum += cur%10
                cur //= 10

            if (cur):
                temp_freq[cur%10] -= 1
                sum += cur
            st += str(sum)
            cur = sum
        temp_freq[cur] -= 1


        if any(x < 0 for x in temp_freq): continue

        ans = ""
        for d in range(1, 10):
            if temp_freq[d] > 0:
                ans += str(d)
                temp_freq[d] -= 1
                break
        for d in range(10):
            ans += str(d) * temp_freq[d]

        print(ans + st)
        break