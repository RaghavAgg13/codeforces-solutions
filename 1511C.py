from sys import stdin, stdout
from collections import deque
input = stdin.readline
print = stdout.write
n,q = list(map(int, input().split()))
a = deque(map(int, input().split()))
t = list(map(int, input().split()))

for i in t:
    num = a.index(i)
    print(str(num+1) + " ")
    del a[num]
    a.appendleft(i)