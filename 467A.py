n = int(input())
count = 0
for i in range(n):
    p_i, q_i = list(map(int, input().split(' ')))  
    if q_i -2 >= p_i:
        count += 1
print(count)