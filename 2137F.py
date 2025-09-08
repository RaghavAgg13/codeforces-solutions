import sys

for _ in range(int(input())):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    final = 0
    for g in range(n):
        
        sub_count = 0
        cur_max = 0
        
        for h in range(g, n):
            max_before_h = cur_max
            
            if a[h] > cur_max:
                cur_max = a[h]

            if a[h] > max_before_h:
                if a[h] == b[h]:
                    sub_count += 1
            else:
                if b[h] <= max_before_h:
                    sub_count += 1
            
            final += sub_count
            
    print(final)