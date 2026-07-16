from collections import defaultdict
for i in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = a.copy()

    hash = defaultdict(int)
    hash[1] = 1
    hash[2] = 1
    while a[0] != 1:
        hash[a[0]] = 1
        if a[0]%2: a[0] += 1
        else: a[0] //= 2
    
    for i in range(1, n):
        set = [1,2]
        while a[i] != 1:
            set.append(a[i])
            if a[i]%2: a[i] += 1
            else: a[i] //= 2

        new_hash = defaultdict(int)
        for i in set:
            if hash[i] == 1:
                new_hash[i] = 1
        hash = new_hash

    # print(hash)
    # print('target', target)

    ans = 1e9
    for target in hash.keys():
        cnt = 0
        for i in b:
            while (i != target):
                if i%2: i += 1
                else: i //= 2
                cnt += 1
        
        ans = min(ans, cnt)

    print(ans)