n, m = list(map(int, input().split()))

days = n
if m == n:
    days += 1
elif n > m:  # n > m
    days = 0
    date = 1
    socks = n
    while socks != 0:
        if date%m == 0:
            socks += 1

        date += 1
        socks -= 1
        days += 1
print(days)