n,m = list(map(int, input().split()))

alpha = n//m
count = n%m
max1 = alpha
max2 = alpha+1
kmin = (m-count)*(max1)*(max1-1)//2 + count*(max2)*(max2-1)//2

max1 = 1
max2 = n-m+1
kmax = (m-1)*(max1)*(max1-1)//2 + (max2)*(max2-1)//2

print(kmin, kmax)