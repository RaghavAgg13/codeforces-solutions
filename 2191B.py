for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    freq = [0]*(n+1)
    for i in a: freq[i] += 1

    if freq[0] == 0: print("NO")
    elif freq[1] > 0: print("YES")
    else: print("YES" if freq[0] == 1 else "NO")
