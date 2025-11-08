from sys import stdin
input = stdin.readline

n,l,a = list(map(int, input().split()))
x,y = 0, 0

breaks = 0
for i in range(n):
    x_,y_ = list(map(int, input().split()))
    delta = x_ - (x+y)
    if delta > 0: breaks += delta//a
    x,y = x_,y_

delta = l-(x+y)
if delta > 0: breaks += delta//a

print(breaks)