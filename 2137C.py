for i in range(int(input())):
    a,b = list(map(int, input().split()))

    final = 1
    if not a%2 and not b%2:
        final = max(a*b//2+2, final)
    elif not b%4:
        final = max(a*b//2+2, final)
    elif a%2 and b%2:
        final = max(a*b+1, final)
    else:
        final = -1

    print(final)