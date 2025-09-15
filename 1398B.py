for i in range(int(input())):
    a = list(input())
    n = len(a)

    even = []
    count = 1
    for i in range(n-1):
        if a[i] != a[i+1]:
            if a[i] == '1': even.append(count)
            count = 1
        else:
            count += 1
    if a[n-1] == '1': even.append(count)

    even.sort(reverse=True)
    s = sum([even[i] for i in range(0, len(even), 2)])
    print(s)