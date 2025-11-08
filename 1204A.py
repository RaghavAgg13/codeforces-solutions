n = int(input(), 2)

cnt = 1
while 4**cnt < n:
    cnt += 1
print(cnt if n > 1 else 0)