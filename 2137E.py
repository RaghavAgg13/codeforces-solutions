from collections import Counter
def mex(arr):
    s = set(arr)
    i = 0
    while True:
        if i not in s:
            return i
        i += 1

for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    history = {tuple(a):0}
    states = [a]

    for i in range(1, k+1):
        counts = Counter(a)
        m = mex(counts)
        a_new = [0] * n

        for j in range(n):
            x = a[j]
            if counts[x] == 1 and x < m:
                a_new[j] = x
            else:
                a_new[j] = m
        a = a_new


        current_tuple = tuple(a)
        if current_tuple in history:
            prev = history[current_tuple]
            cycle_len = i- prev

            rem_k = k-i
            final_idx = prev + (rem_k%cycle_len)

            final_list = states[final_idx]
            print(sum(final_list))
            break

        history[current_tuple] = i
        states.append(a)

        
    else: print(sum(a))