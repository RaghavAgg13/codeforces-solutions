for i in range(int(input())):
    n = int(input())

    prevCount = 0
    b = ''
    for i in range(n):
        a = input()
        if '1' in a:
            count = a.count('1')
            if prevCount != 0 and b == '':
                if count == prevCount:
                    b = 'SQUARE'
                else:
                    b = 'TRIANGLE'
            else:
                prevCount = count

    print(b)