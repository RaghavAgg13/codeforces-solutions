n = int(input())
a = list(map(int, input().split()))

b = sorted(a)

low = (n+1)//2
# check = True
# for i in range(n//2):
#     if a[i] > a[i+low]:
#         check = False
#         break

# for i in range(1, n//2):
#     if a[i+n//2] < a[i]:
#         check = False
#         break

c = [0]*n
cnt = 0
for i in range(0, n, 2):
    c[i] = b[cnt]
    if cnt+low < n: c[i+1] = b[cnt+low]
    cnt += 1

for i in range(1, n-1, 2):
    if not (c[i-1] <= c[i] >= c[i+1]):
        print('Impossible')
        break
else:
    print(*c)