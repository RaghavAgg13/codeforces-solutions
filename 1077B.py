n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(n-2, 0, -1):
    if a[i] == 0 and a[i+1] == a[i-1] == 1:
        cnt += 1
        a[i-1] = 0

print(cnt)    

    

