for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count,carry = 0,0
    for i in range(n):
        if a[i] <= 0:
            carry += 1
        else:
            if a[i-carry:i] == [0]*carry: count += 0
            elif carry: count += 1
            carry = 0

    if a[n-carry:n] == [0]*carry: count += 0
    elif carry: count += 1

    s = sum([abs(a[i]) for i in range(n)])
    print(s, count)