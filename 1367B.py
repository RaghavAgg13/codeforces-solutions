t = int(input())

for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    defectors = {}
    for i in range(n):
        if i % 2 != s[i] % 2:
            defectors[i] = s[i]
    # print(defectors)

    if len(defectors) == 0:
        print('0')
        continue

    count_ind_even, count_val_even = 0,0
    for i in defectors:
        if i % 2 == 0: count_ind_even += 1
        if defectors[i]%2 == 0: count_val_even += 1

    if count_ind_even == count_val_even:
        print(count_ind_even)
    else:
        print('-1')