n,k = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))

if k == 0 and a[0]>1:
    print(a[0]-1)
elif n==k:
    print(a[-1])
elif a[k]-a[k-1] >= 1: 
    print(a[k-1])
else: print('-1')