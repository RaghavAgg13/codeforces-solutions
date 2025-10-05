n = int(input())

left_open, right_open = 0,0

for i in range(n):
    l,r = list(map(int, input().split()))
    left_open += l
    right_open += r

print(min(n-left_open, left_open)+min(n-right_open, right_open))