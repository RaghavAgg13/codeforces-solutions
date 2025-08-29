for i in range(int(input())):
    a = input()

    if '1' in a:
        start = a.index('1')
        end = len(a)-a[::-1].index('1')
        count = a[start:end].count('0')
        print(count)
    else:
        print(0)