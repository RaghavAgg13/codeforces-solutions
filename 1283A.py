for i in range(int(input())):
    h, m = list(map(int, input().split()))
    print((24-h)*60 - m)