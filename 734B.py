k2,k3,k5,k6 = list(map(int, input().split()))

s1 = min(k2,k5,k6)*256
a = min(k2,k5,k6)
if k2 >= a: s1 += min(k2-a, k3)*32


print(s1)