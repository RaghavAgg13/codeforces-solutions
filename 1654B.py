for _ in range(int(input())):
    a = input()

    pos = 0

    freq = {}
    for i in a:
        freq[i] = freq.get(i, 0) + 1

    while pos < len(a) and freq[a[pos]] > 1:
        freq[a[pos]] -= 1
        pos += 1
    
    print(a[pos:])