n = int(input())
cap = 0
l = [0]
for i in range(n):
    a_i, b_i = list(map(int, input().split(' ')))
    cap += b_i - a_i
    l.append(cap)
print(max(l))