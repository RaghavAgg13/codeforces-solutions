w,h,k = list(map(int, input().split()))

i = 0
cnt = 0
while (min(w,h) > 4*i and i < k):
    cnt += 2*(w-4*i + h-4*i - 2)
    i += 1

print(cnt)