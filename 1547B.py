for i in range(int(input())):
    a = input()

    n = len(a)
    check = True

    for i in range(n):
        if chr(i+97) not in a:
            check = False
            break

    if check:
        start = 0
        end = n-1
        count = 1
        while start < end:
            if ord(a[start])-97 == n-count:
                count += 1
                start += 1
            elif ord(a[end])-97 == n-count:
                count += 1
                end -= 1
            else:
                check = False
                break

    print('YES' if check else 'NO')