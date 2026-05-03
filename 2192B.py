for i in range(int(input())):
    n = int(input())
    a = list(input())

    even, odd = [], []
    for i in range(n):
        if a[i] == "1":
            even.append(i)
        else:
            odd.append(i)

    if len(even)%2 == 0:
        print(len(even))
        for i in even:
            print(i+1, end = ' ')
        print()
    elif len(odd)%2:
        print(len(odd))
        for i in odd:
            print(i+1, end = ' ')
        print()
    else:
        print(-1)   