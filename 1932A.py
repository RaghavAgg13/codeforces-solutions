for i in range(int(input())):
    n = int(input())
    a = input()

    count = 1 if a[0] == '@' else 0
    i = 1
    while i < n:
        if a[i] == "@":
            count += 1
            i += 1
        elif i+1<n and a[i+1] == '@':
            count += 1
            i += 2
        elif i+1<n and a[i+1] == ".":
            i += 2
        elif a[i] == ".":
            i += 1
        else:
            break

    print(count)