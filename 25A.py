n = int(input())
l = list(map(int, input().split()))

even = [False]*n
for i in range(n):
    even[i] = True if l[i]%2 == 0 else False

# print(even)
if even.count(True) == 1: print(even.index(True)+1)
elif even.count(False) == 1: print(even.index(False)+1)