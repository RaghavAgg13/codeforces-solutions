from collections import defaultdict

for i in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))

    groups = defaultdict(list)
    for i, val in enumerate(b):
        groups[val].append(i)

    is_possible = True
    for k, indices in groups.items():
        if len(indices) % k != 0:
            is_possible = False
            break 

    if not is_possible:
        print(-1)
    else:
        a = [0] * n
        value_to_assign = 1
        
        for k in sorted(groups.keys()):
            indices = groups[k]
            for i in range(0, len(indices), k):
                for j in range(k):
                    a[indices[i+j]] = value_to_assign
                value_to_assign += 1
                
        print(*a)