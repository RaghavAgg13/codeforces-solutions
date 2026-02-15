n,k = list(map(int, input().split()))
a = list(map(int, input().split()))

step = n//k
arr = [0]*k
arr_ = [0]*k
for i in range(k):
    for j in range(i, n, k):
        # print(a[j], end=' ')
        if a[j] == 1: arr[i] += 1  
        else: arr_[i] += 1 
    # print()

for i in range(k):
    arr[i] = min(arr[i], arr_[i])

if k == 1:
    print(min(a.count(1), a.count(2)))
else:
    print(sum(arr))