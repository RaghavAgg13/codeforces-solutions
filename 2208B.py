import heapq

for i in range(int(input())):
    n, k, p, m = list(map(int, input().split()))
    a = list(map(int, input().split()))

    win_val = a[p-1]

    cur_pos = p
    t_cost = 0
    cnt = 0

    while (t_cost < m):
        if (cur_pos <= k):
            t_cost += win_val
            if t_cost > m:
                break

            a.pop(cur_pos - 1)
            a.append(win_val)
            cnt += 1
            cur_pos = n
        else:
            while (cur_pos > k):
                val = a.pop(a.index(min(a[:k])))
                t_cost += val
                if t_cost > m:
                    break
                
                a.append(val)
                cur_pos -= 1

    print(cnt)