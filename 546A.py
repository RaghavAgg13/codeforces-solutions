k, n, w = list(map(int, input().split(' ')))

total_cost = w*(w+1)*k/2
if total_cost > n:
    print(int(total_cost-n))
else:
    print('0')