from sys import stdin, stdout
input = stdin.readline

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    cream = 0

    for i in range(n-1, -1, -1):
        cream = max(cream, a[i])
        if cream > 0:
            a[i] = 1
            cream -= 1
        
    print(*a)