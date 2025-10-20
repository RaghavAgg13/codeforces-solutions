for _ in range(int(input())):
    n = int(input())

    org_sum = (n*(n+1))//2
    print(2, 1, n)
    new_sum = int(input())

    gap = new_sum-org_sum

    # i = 1
    # while i < n+2-gap:
    #     print(2, i, i+gap-1, flush=True)
    #     new = int(input())
    #     print(1, i, i+gap-1, flush=True)
    #     old = int(input())

    #     if new == old+gap:
    #         print("!", i, i+gap-1, flush=True)
    #         break
    #     elif old != new:
    #         print("!", i+gap-new+old, i+gap+gap-new+old-1, flush=True)
    #         break
    #     else:
    #         i += gap-1
    #     i+= 1

    low, high = 1,n
    start_pos = n

    while low <= high:
        mid = (high+low)//2

        print(2, 1, mid)
        new = int(input())
        print(1, 1, mid)
        old = int(input())

        diff = new-old

        if diff:
            start_pos = mid
            high = mid-1
        else:
            low = mid+1

    end_pos = start_pos+gap-1
    print("!", start_pos, end_pos)