n,q = list(map(int, input().split()))
a = input()

sum = [0]
for i in range(n):
    sum.append(sum[-1]+ord(a[i])-96)

for i in range(q):
    l,r = list(map(int, input().split()))
    # b = a[l-1:r]
    
    print(sum[r]-sum[l-1])