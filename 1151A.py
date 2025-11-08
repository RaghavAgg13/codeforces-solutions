def f(i, x): return min(abs(a[i]-x), 26-abs(a[i]-x))

n = int(input())
word = input()
a = []
for i in word:
    a.append(ord(i))

# print(a)

m = f(0,65) + f(1,67) + f(2,84) + f(3, 71)
for i in range(1, n-3):
    m = min(m, f(0+i,65) + f(1+i,67) + f(2+i,84) + f(3+i, 71))

print(m)