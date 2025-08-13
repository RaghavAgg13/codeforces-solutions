n,m,a,b = list(map(int, input().split(' ')))
soln = [0]
cost = 0

if n % m == 0:
    cost_1 =  (n // m) * b
    cost_2 = n * a
    cost = min(cost_1, cost_2)
else:
    cost_1 = (n // m + 1) * b
    cost_2 = (n // m) * b + (n % m) * a
    cost = min(cost_1, cost_2)

print(cost)