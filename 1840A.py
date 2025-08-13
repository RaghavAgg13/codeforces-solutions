for i in range(int(input())):
    n = int(input())
    a = input()
    s = ""

    cur = a[0]
    idx = 0
    for i in range(1, n-1):
        letter = a[i]

        if letter == cur and idx != i:
            s += cur
            cur = a[i+1]
            idx = i+1

    if a[-1] == cur and idx != n-1:
        s += cur

    print(s)