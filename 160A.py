n = int(input())
coins = sorted(list(map(int, input().split(' '))), reverse=True)
soln = []
for i in range(len(coins)):
    if len(coins) > 1:
        if sum(coins[:i+1]) > sum(coins[i+1:]):
            soln.append(i+1)
    else:
        soln.append(1)
print(min(soln))