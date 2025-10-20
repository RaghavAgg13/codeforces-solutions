l,r = list(map(int, input().split()))

check = 1
for i in range(l, r+1):
    if len(list(str(i))) == len(set(str(i))):
        print(i)
        check = 0
        break

if check: print(-1)