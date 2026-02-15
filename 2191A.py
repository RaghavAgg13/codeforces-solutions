for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    freq = [0]*101
    # for i in range(n):
        # freq[a[i]] = 1
    

    for i in range(n):
        if i%2: freq[a[i]] = 1
        else: freq[a[i]] = -1
    a.sort()

    for i in range(n-1):
        if freq[a[i]] == freq[a[i+1]]:
            print("NO")
            break
    else:
        print("YES")