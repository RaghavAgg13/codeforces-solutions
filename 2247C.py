for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    indices = set()
    odd_cnt = 0
    for i in range(n):
        if a[i] != b[i]:
            indices.add(i)
            if a[i]: odd_cnt += 1
    cnt = len(indices)

    # if no of swaps are <= k, then it depends solely on the number of 
    # ones if odd_cnt is odd, then its perfect
    # since we can choose any such k, then at one pass we can choose
    # any 0's to be swapped right

    # best case scenario
    if a == b:
        print(0)
    elif odd_cnt%2:
        print(1)
    else:
        # now this is tricky
        # if we have a one(s) (and its gonna be > 1, not 1 cause above)
        # so we can split this as 1) one and 2) the remaining
        if odd_cnt:
            print(2)
        # cnt = 0
        else:
            # no way out - no way out
            if cnt == n or 1 not in a:
                print(-1)
            # if we take a zero and a one not in incides, it works in 2
            elif cnt <= n-2:
                x = False
                for i in range(n):
                    if a[i] == 0 and i not in indices:
                        x = True
                        break
                print(2 if x else -1)
            else:
                print(-1)
            
    
