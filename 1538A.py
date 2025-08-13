for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    idx1 = a.index(min(a))+1
    idx2 = a.index(max(a))+1
    count = 0

    #(idx1, idx2, n-idx1+1, n-idx2+1)
    pt1 = min(idx1, idx2, n-idx1+1, n-idx2+1)

    if idx1 == pt1 or n-idx1+1 == pt1:
        if idx1 == pt1:
            count += idx1
            a = a[idx1:]
        else:
            count += n-idx1+1
            a = a[:idx1-1]

        idx2 = a.index(max(a))+1
        if min(idx2, len(a)-idx2+1) == idx2: count += idx2
        else: count += len(a)-idx2+1
    else:
        if idx2 == pt1:
            count += idx2
            a = a[idx2:]
        else:
            count += n-idx2+1
            a = a[:idx2-1]

        idx1 = a.index(min(a))+1
        if min(idx1,len(a)-idx1+1) == idx1: count += idx1
        else: count += len(a)-idx1+1

    print(count)