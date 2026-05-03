a = input()
b = input()

l = len(b)
cnt = 0

cur = ""
n = len(a)
start = 0
for i in range(n):
    if (i-start+1 > l): start += 1
    if (a[start:i+1] == b):
        cnt += 1
        start = i+1
    


print(cnt)
