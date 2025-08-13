for i in range(int(input())):
    n = int(input())
    s = input()

    start = s.index('B')
    s = s[-1:-n-1:-1]
    end = n - s.index('B')
    print(end-start)
