n = input()

cnt = 0
while len(str(n)) > 1:
    s = str(sum([int(i) for i in n]))
    n = s
    cnt += 1

print(cnt)